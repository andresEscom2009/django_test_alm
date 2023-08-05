from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    web_site = models.CharField(max_length=255, blank=True)
    # pass

    USERNAME_FIELD = 'email'  # Se va a loggear por medio del email en lugar del username
    REQUIRED_FIELDS = []