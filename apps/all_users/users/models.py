from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.all_users.users.managers import UserManager

from core.models import BaseModel


class UserModel(AbstractBaseUser, BaseModel, PermissionsMixin):
    class Meta:
        db_table = 'auth_users'

    email = models.EmailField(unique=True, db_index=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    birth_date = models.DateField()
    phone = models.CharField(max_length=15, unique=True, db_index=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')


