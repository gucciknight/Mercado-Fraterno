from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
#from django.db import transaction
#from django.db.models import Count
from django.urls import reverse
#from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, FormView
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404


#from ..decorators import student_required
from ..forms import SignUpForm
from ..models import User, Participant, Administrator, Coin, CoinBalance, Transaction



class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        coin = Coin.objects.get(pk = self.request.POST['coins'])
        new_coin_balance = CoinBalance(user=user, coin=coin, offer=self.request.POST['offer'], balance=coin.base_quantity)
        new_coin_balance.save()
        coin_list = CoinBalance.objects.filter(user=user)
        login(self.request, user)
        return render(self.request, 'market/coins.html', {
            "user" : user,
            "coin_list" : coin_list,
        })

@login_required
def user_validation(request, coin_balance_id):

    coin_balance = get_object_or_404(CoinBalance, pk=coin_balance_id)
    coin_balance.is_validated = True

    return HttpResponseRedirect(reverse("core:transaction_view", args=(new_transaction.pk,)))

class SignUpViewInvitation(FormView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup_invitation_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coin_id'] = kwargs['coin_id']
        return context
    
    def get_form_kwargs(self):
        kwargs = super(SignUpViewInvitation, self).get_form_kwargs()
        kwargs['coin_id'] = self.kwargs.get('coin_id')
        return kwargs

    def form_valid(self, form):
        user = form.save()
        coin = Coin.objects.get(pk = self.request.POST['coins'])
        new_coin_balance = CoinBalance(user=user, coin=coin, offer=self.request.POST['offer'], balance=coin.base_quantity)
        new_coin_balance.save()
        coin_list = CoinBalance.objects.filter(user=user)
        login(self.request, user)
        return render(self.request, 'market/coins.html', {
            "user" : user,
            "coin_list" : coin_list,
        })