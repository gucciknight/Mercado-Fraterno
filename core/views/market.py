import re
from tkinter import E
from django import forms
from django.db.models import Exists, OuterRef, Q
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..models import User, Participant, Administrator, Coin, CoinBalance, Transaction
from core.forms import CoinCreationForm

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
    context_object_name = 'coin_balance'
    template_name = 'market/market.html'

    def get_context_data(self,**kwargs):
        coin_balance = self.get_object()
        actual_coin = coin_balance.coin.name
        coin_id = coin_balance.coin.id
        balance = coin_balance.balance
        coin_offer = coin_balance.offer
        coin_participants_with_this_user = CoinBalance.objects.filter(coin = coin_balance.coin)
        coin_participants = coin_participants_with_this_user.exclude(user = coin_balance.user)
        coin_history = Transaction.objects.filter(sender = coin_balance).filter(is_validated=True).order_by("-date")
        coin_movements = Transaction.objects.filter(sender__coin_id = coin_id).filter(is_validated=True).order_by("-date")
        extra_context = {
            "actual_coin": actual_coin,
            "coin_id": coin_id,
            "coin_balance": balance,
            "coin_offer": coin_offer,
            "coin_participants": coin_participants,
            "coin_balance_id": coin_balance.pk,
            "coin_history": coin_history, 
            "coin_movements": coin_movements,
        }
        kwargs.update(extra_context)
        return super().get_context_data(**kwargs)

def transference(request, coin_balance_id):

    user_coin_balance = get_object_or_404(CoinBalance, pk=coin_balance_id)
    
    try:
        data = request.POST.copy()
        #data["coin_user"] = request.POST["coin_user"]
        reciever_user = User.objects.get(pk=data["coin_user"])
        ammount_transfered = int(data['coin_ammount'].replace('.',''))
    except (KeyError, CoinBalance.DoesNotExist):
        error_message = 'hola'
        return HttpResponseRedirect(reverse("core:coin_list", args=(coin_id,)))
    else:
        coin_id = user_coin_balance.coin.pk
        if ammount_transfered > (user_coin_balance.balance):

            return HttpResponseRedirect(reverse("core:coin_list", args=(coin_balance_id, )))
        else:
            
            reciever_coin_balances = CoinBalance.objects.filter(user=reciever_user)
            reciever_coin_balance = reciever_coin_balances.get(coin=user_coin_balance.coin)

            user_coin_balance.balance = user_coin_balance.balance - ammount_transfered
            user_coin_balance.save()
            reciever_coin_balance.balance = reciever_coin_balance.balance + ammount_transfered
            reciever_coin_balance.save()
        
            new_transaction = Transaction(sender=user_coin_balance, reciever=reciever_coin_balance, ammount=ammount_transfered, date=datetime.now(), is_validated=False)
            new_transaction.save()
            
            return HttpResponseRedirect(reverse("core:transaction_view", args=(new_transaction.pk,)))

class TransactionView(DetailView):
    model = Transaction
    context_object_name = 'transaction_detail'
    template_name = 'market/transaction_detail.html'

    def get_context_data(self, **kwargs):
        transaction_object = self.get_object()
        extra_context = {
            "transaction_object": transaction_object,
        }
        kwargs.update(extra_context)
        context = super().get_context_data(**kwargs)
        return context

def transference_validated(request, transaction_id):

    transaction = get_object_or_404(CoinBalance, pk=transaction_id)
    transaction.update(is_validated=True)

    coin_balance = CoinBalance.objects.get(coin_id = transaction.sender_id)
    return render(request, 'core:market', {
        'coin_balance': coin_balance,
    })
    
    
class CoinCreationView(CreateView):
    model = Coin
    form_class = CoinCreationForm
    context_object_name = 'coin_form'
    template_name = 'market/createcoin.html'


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