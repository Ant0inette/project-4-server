from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=40)
    username = models.CharField(max_length=10, unique=True)
    profile_image = models.CharField(max_length=250)


# Create your models here.
