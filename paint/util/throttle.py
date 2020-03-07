'''Custom throttle subclasses to allow independent configuration

DRF only allows a DEFAULT_THROTTLE_RATES setting which applies to all
throttles equally, but we want to be able to configure each one separately.
'''

from django.conf import settings
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AnonymousThrottle(AnonRateThrottle):
    rate = settings.THROTTLE_ANON

class UserThrottle(UserRateThrottle):
    rate = settings.THROTTLE_USER
