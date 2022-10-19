from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..models import User, Participant, Administrator, Coin, CoinBalance, Transaction
# Create your views here.
def home(request):
    #coin_list = Coin.objects.filter(coin = coin_balance_list)
    #user_coins = request.
    if request.user.is_authenticated:
        user_name = request.user.first_name
        coin_list = CoinBalance.objects.filter(user=request.user)
        return render(request, 'market/coins.html', {
            "user_name": user_name,
            "coin_list": coin_list
        })
    return render(request, 'home.html')

class CoinListView(ListView):
    def get_associated_coins(self):
        coin_list = self.request.coin.name
        return coin_list

class MarketView(DetailView):
    model = CoinBalance
    context_object_name = 'transaction_market'
    template_name = 'market/market.html'

    def get_context_data(self,**kwargs):
        coin_balance = self.get_object()
        actual_coin = coin_balance.coin.name
        coin_id = coin_balance.coin.id
        balance = coin_balance.balance
        coin_offer = coin_balance.offer
        extra_context = {
            "actual_coin": actual_coin,
            "coin_id": coin_id,
            "coin_balance": balance,
            "coin_offer": coin_offer
        }
        kwargs.update(extra_context)
        return super().get_context_data(**kwargs)

    def get_balance():
        return

'''
@method_decorator(login_required, name='dispatch')
class CoinListView(ListView):
    model = Coin
    ordering = ('name', )
    context_object_name = 'coins'
    template_name = 'classroom/teachers/quiz_change_list.html'

    def get_queryset(self):
        queryset = self.request.user.quizzes \
            .select_related('subject') \
            .annotate(questions_count=Count('questions', distinct=True)) \
            .annotate(taken_count=Count('taken_quizzes', distinct=True))
        return queryset        
'''