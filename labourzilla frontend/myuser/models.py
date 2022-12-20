from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class customuser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length= 255, unique=True)
    contact_no = models.IntegerField(null=True, unique=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

