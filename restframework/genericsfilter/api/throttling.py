from rest_framework.throttling import UserRateThrottle

class JackRateThrottling(UserRateThrottle):
    scope = 'jack'