'''
Custom User implementation.

We cannot use typing effectively here due to Django QuerySet and 
BaseManager not having __class_getitem__. 

See here for more info:
https://github.com/django/django/pull/12405
'''

from __future__ import annotations

from typing import TypeVar

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

### Manager ###################################################################

# will be un-commented and used when Django #12405 is merged
# T = TypeVar('T', bound=AbstractBaseUser, covariant=True) 

class UserManager(BaseUserManager):
    """Custom manager for our User model
    
    If using MyPy, this implementation might spring type errors 
    due to  this PR not being merged:
    https://github.com/django/django/pull/12405
    """

    def create_user(self, identifier: str, password: str = None) -> 'User':
        if not identifier:
            raise ValueError("Users must have an identifier")

        user: 'User' = self.model(identifier=identifier) # type: ignore

        user.set_password(password)
        user.save()
        return user

### User ######################################################################

class User(AbstractBaseUser):
    """Custom User with a custom identifier field
    
    Usernames and emails are not relevant to factories, so we
    customize the User model to suit our domain.
    """
    identifier: models.CharField = models.CharField(max_length=255, unique=True)
    is_admin: models.BooleanField = models.BooleanField(default=False)

    objects: UserManager = UserManager()

    USERNAME_FIELD: str = 'identifier'

    def __str__(self: User):
        return f'<user:{self.identifier}>'
