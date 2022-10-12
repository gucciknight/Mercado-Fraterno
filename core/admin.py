from django.contrib import admin
from .models import User, Participant, Administrator, Coin, CoinBalance, Transaction

admin.site.register(User)
admin.site.register(Participant)
admin.site.register(Administrator)
admin.site.register(Coin)
admin.site.register(CoinBalance)
admin.site.register(Transaction)
# Register your models here.
