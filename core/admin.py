from django.contrib import admin
from .models import User, Participant, Administrator, Coin, CoinBalance, Transaction
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _



admin.site.register(User)
admin.site.register(Participant)
admin.site.register(Administrator)
admin.site.register(Coin)
admin.site.register(CoinBalance)
admin.site.register(Transaction)
# Register your models here.


#@admin.site.unregister(Administrator)

