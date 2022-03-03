from rest_framework.authentication import TokenAuthentication

from hello_backend.settings import ACCESS_TOKEN_KEY


class TokenAuthSupportCookie(TokenAuthentication):
    """
    Extend the TokenAuthentication class to support cookie based authentication
    """

    def authenticate(self, request):
        if 'HTTP_AUTHORIZATION' in request.META:
            return super().authenticate(request)

        if ACCESS_TOKEN_KEY in request.COOKIES:
            return self.authenticate_credentials(
                request.COOKIES.get(ACCESS_TOKEN_KEY)
            )

        return super().authenticate(request)
