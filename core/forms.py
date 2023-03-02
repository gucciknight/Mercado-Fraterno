from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from core.models import ( Participant, Administrator, 
                        Coin, CoinBalance, Transaction, User)

class SignUpForm(UserCreationForm):
    whatsapp = forms.CharField(max_length=8, help_text='Número de 8 dígitos, sin código de país ni anteponer 9', label='Número de Celular')
    first_name = forms.CharField(max_length=32, label='Nombre')
    last_name = forms.CharField(max_length=32, label='Apellido')
    username = forms.HiddenInput
    email = forms.CharField()
    coins = forms.ChoiceField(widget=forms.Select, choices=Coin.objects.all().values_list('id', 'name'), label='Moneda a la que quiere participar')
    offer = forms.CharField(max_length=50, help_text='Nombre de forma breve, lo que va a ofrecer en mercado fraterno', label='Que voy a ofrecer')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [ 'first_name', 'last_name', 'password1', 'password2', 'whatsapp', 'email', 'coins']

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email   

class CoinCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=32, label='Nombre')
    #caca = forms.CharField(max_length=32, label='Nombre')
    class Meta:
        model = Coin
        fields = ('name', 'base_quantity',)