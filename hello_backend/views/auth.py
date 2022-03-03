from logging import getLogger
from urllib.parse import urlencode

from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _
from hello_backend.serializers.auth import GoogleLoginSerializer
from hello_backend.services.auth import (get_access_token_google,
                                         get_user_info_google)
from hello_backend.services.user import get_or_create_token, get_or_create_user
from hello_backend.settings import ACCESS_TOKEN_KEY

User = get_user_model()

_logger = getLogger(__name__)


class GoogleLoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('code', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('error', openapi.IN_QUERY, type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request, *args, **kwargs):
        _logger.info(_('Test logging'))
        request_serializer = GoogleLoginSerializer(data=request.GET)
        request_serializer.is_valid(raise_exception=True)

        validated_data = request_serializer.validated_data

        code = validated_data.get('code')
        error = validated_data.get('error')

        if error or not code:
            params = urlencode({'error': error})
            return redirect(f'{settings.BASE_FRONTEND_URL}/login?{params}')

        access_token = get_access_token_google(
            code=code,
            redirect_uri=f'{settings.BASE_BACKEND_URL}{reverse("login-with-google")}'
        )

        user_data = get_user_info_google(access_token=access_token)
        user_data = {
            'email': user_data['email'],
            'first_name': user_data.get('givenName', ''),
            'last_name': user_data.get('familyName', ''),
        }

        user = get_or_create_user(**user_data)
        token = get_or_create_token(user_id=user.id)

        response = redirect(f'{settings.BASE_FRONTEND_URL}')
        response.set_cookie(ACCESS_TOKEN_KEY, token, domain=settings.COOKIE_DOMAIN, secure=True, httponly=True)
        return response
