from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField()

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'email'
    ]

    def __str__(self):
        return self.username

    