from django.conf import settings
from django.db import models


class UserLogin(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)


# Create your models here.
