from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=20)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    skills = models.CharField('Навыки', max_length=100)
    # add additional fields in here