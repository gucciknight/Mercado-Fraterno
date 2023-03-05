from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None
    whatsapp = models.CharField(max_length=30)
    email = models.EmailField(_('email address'), unique=True)
    objects = UserManager()
    

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="participant")
    is_admited = models.BooleanField(default=False)


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    USERNAME_FIELD = 'email'



class Coin(models.Model):
    name = models.CharField(max_length=20)
    base_quantity = models.IntegerField()
    is_validated = models.BooleanField(default=False)


class CoinBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coin_user')
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='user_balance')
    offer = models.CharField(max_length=10000)
    balance = models.IntegerField()
    transactions_made = models.IntegerField(default=False)
    

class Transaction(models.Model):
    sender = models.ForeignKey(CoinBalance, on_delete=models.CASCADE, related_name='sender_user')
    reciever = models.ForeignKey(CoinBalance, on_delete=models.CASCADE, related_name='reciever_user')
    ammount = models.IntegerField()
    date = models.DateTimeField("transaction datails")
    is_validated = models.BooleanField()