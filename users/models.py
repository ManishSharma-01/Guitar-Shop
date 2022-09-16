from doctest import FAIL_FAST
from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
    

class CustomUser(AbstractUser):
    gender = models.CharField( max_length=10)
    phone_number = models.CharField(max_length=10)
    