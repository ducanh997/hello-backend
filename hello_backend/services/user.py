from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


def create_user(email, password=None, **extra_fields) -> User:
    extra_fields = {
        'is_staff': False,
        'is_superuser': False,
        **extra_fields
    }

    user = User(email=email, username=email, **extra_fields)

    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()

    user.full_clean()
    user.save()

    return user


def get_or_create_user(email, password=None, **extra_fields) -> User:
    user = User.objects.filter(email=email).first()
    if not user:
        user = create_user(email=email, password=password, **extra_fields)

    return user


def get_or_create_token(user_id) -> Token:
    token = Token.objects.filter(user_id=user_id).first()
    if not token:
        token = Token.objects.create(user_id=user_id)

    return token
