from tkinter import CASCADE
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
    base_quantity = models.IntegerField()


class CoinBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coin_user')
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='user_balance')
    offer = models.CharField(max_length=10000)
    balance = models.IntegerField()
    


class Transaction(models.Model):
    sender = models.ForeignKey(CoinBalance, on_delete=models.CASCADE, related_name='sender_user')
    reciever = models.ForeignKey(CoinBalance, on_delete=models.CASCADE, related_name='reciever_user')
    ammount = models.IntegerField()
    date = models.DateTimeField("transaction datails")