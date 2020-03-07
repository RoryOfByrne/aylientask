from django.urls import path

from paint.apps.authentication.views import CreateAccount

v2 = [
    path('register/', CreateAccount.as_view(), name='v2-authentication-register')
]