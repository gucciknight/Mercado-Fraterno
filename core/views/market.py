from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
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
        coin_participants_with_this_user = CoinBalance.objects.filter(coin = coin_balance.coin)
        coin_participants = coin_participants_with_this_user.exclude(user = coin_balance.user)
        extra_context = {
            "actual_coin": actual_coin,
            "coin_id": coin_id,
            "coin_balance": balance,
            "coin_offer": coin_offer,
            "coin_participants": coin_participants,
            "coin_balance_id": coin_balance.pk
        }
        kwargs.update(extra_context)
        return super().get_context_data(**kwargs)

def transference(request, coin_balance_id):

    user_coin_balance = get_object_or_404(CoinBalance,pk=coin_balance_id)
    
    try:
        reciever_user = User.objects.get(pk=request.POST["coin_user"])
        ammount_transfered = request.POST["coin_ammount"]
    except (KeyError, CoinBalance.DoesNotExist):
        return render(request, "market/market.html", {
            "question": reciever_user,
            "error_message": "No elegiste una respuesta"
        })
    else:
        reciever_coin_balances = CoinBalance.objects.filter(user=reciever_user)
        reciever_coin_balance = reciever_coin_balances.get(coin=user_coin_balance.coin)

        user_coin_balance.balance = user_coin_balance.balance - int(ammount_transfered)
        user_coin_balance.save()
        reciever_coin_balance.balance = reciever_coin_balance.balance + int(ammount_transfered)
        reciever_coin_balance.save()
        
        new_transaction = Transaction(sender=user_coin_balance,reciever=reciever_coin_balance,ammount=ammount_transfered,date=datetime.now())
        new_transaction.save()

        return HttpResponseRedirect(reverse("core:transaction_view", args=(new_transaction.pk,)))

class TransactionView(DetailView):
    model = Transaction
    context_object_name = 'transaction_detail'
    template_name = 'market/transaction_detail.html'

    def get_context_data(self, **kwargs):
        hola = self.get_object()
        extra_context = {
            "hola": hola
        }
        kwargs.update(extra_context)
        context = super().get_context_data(**kwargs)
        return context
    
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