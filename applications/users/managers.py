from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager, models.Manager):
    def _create_user(
        self,
        first_name,
        last_name,
        username,
        email,
        password,
        is_staff,
        is_superuser,
        **extra_fields
    ):
        user = self.model(
            first_name=first_name.capitalize(),
            last_name=last_name.capitalize(),
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        # Token.objects.get_or_create(user=user)
        user.save(using=self.db)

        return user

    def create_user(
        self,
        first_name,
        last_name,
        username,
        email,
        password=None,
        **extra_fields
    ):
        return self._create_user(
            first_name,
            last_name,
            username,
            email,
            password,
            False,
            False,
            **extra_fields
        )
    def create_superuser(
        self,
        first_name,
        last_name,
        username,
        email,
        password=None,
        **extra_fields
    ):
        return self._create_user(
            first_name,
            last_name,
            username,
            email,
            password,
            True,
            True,
            **extra_fields
        )


    