from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class GolfUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    display_name = models.CharField(verbose_name="display name", max_length=15)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name']
