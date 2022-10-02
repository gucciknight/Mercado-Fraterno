from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    whatsapp = models.CharField(max_length=30)
    

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="participant")
    is_admited = models.BooleanField(default=False)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Coin(models.Model):
    name = models.CharField(max_length=20)
    base_quantity = models.IntegerField(max_length=30)