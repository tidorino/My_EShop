from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone

from My_EShop.accounts.managers import EShopUserManager


class EShopUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
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
        return self.email

