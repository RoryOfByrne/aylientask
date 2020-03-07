from typing import cast

from django.contrib.auth import get_user_model

from paint.apps.authentication.types import UserModelType


def get_typed_user_model() -> UserModelType:
    return cast(UserModelType, get_user_model())