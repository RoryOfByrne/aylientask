from typing import Dict

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from paint.apps.authentication.models import User
from paint.apps.authentication.types import UserModelType
from paint.apps.authentication.util import get_typed_user_model

class UserSerializer(serializers.ModelSerializer):
    """Serializes Users to JSON"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_typed_user_model()
        fields = ('identifier', 'password')

    ### General Methods ##############################################

    def create(self, validated_data: Dict[str, str]) -> User:
        """Create and return the new user"""
        UserModel: UserModelType = self.Meta.model
        user: User = UserModel.objects.create_user(
            identifier=validated_data['identifier'],
            password=validated_data['password']
        )
        user.save()

        return user

    ### Field Methods ##############################################

    def validate_password(self, password: str) -> None:
        try:
            validate_password(password)
        except ValidationError as e:
            # join all possible validation issues into one string
            raise serializers.ValidationError(' '.join(e.messages))