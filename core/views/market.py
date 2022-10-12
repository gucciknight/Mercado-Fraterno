from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..models import User, Participant, Administrator, Coin, CoinBalance, Transaction
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'market/coins.html')
    return render(request, 'home.html')


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
        
