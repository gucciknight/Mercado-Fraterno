from django.contrib import admin
from .models import User
from .models import Participant
from .models import Admin
from .models import Coin
from .models import CoinBalance
from .models import Transaction

admin.site.register(User)
admin.site.register(Participant)
admin.site.register(Admin)
admin.site.register(Coin)
admin.site.register(CoinBalance)
admin.site.register(Transaction)
# Register your models here.
