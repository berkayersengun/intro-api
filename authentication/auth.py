from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from main import settings


def refreshToken(request):
    raw_token = request.COOKIES.get(settings.SIMPLE_JWT['COOKIE_REFRESH']) or None
    if raw_token is None:
        return None
    token = RefreshToken.for_user(request.user).access_token
    return token


class CustomAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        # enforce_csrf(request)
        if header is None:  # Check cookies first (UI)
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['COOKIE_ACCESS']) or None
        else:
            raw_token = self.get_raw_token(header)  # get from header (rest)

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token
