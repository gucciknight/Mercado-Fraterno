from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from core.models import ( User, Participant, Administrator, 
                        Coin, CoinBalance, Transaction)

class AdministratorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
