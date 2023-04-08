from django.db import models
from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.utils import timezone

from My_EShop.accounts.managers import EShopUserManager
from My_EShop.core.validators import validate_only_letters


class EShopUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MAX_LEN_NAME = 30
    MIN_LEN_NAME = 2

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        default=timezone.now,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'

    objects = EShopUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



