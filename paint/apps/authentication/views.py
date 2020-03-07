from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from paint.apps.authentication.serializers import UserSerializer
from paint.apps.authentication.util import get_typed_user_model


class CreateAccount(CreateAPIView):
    """Creates a new account"""

    model = get_typed_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
