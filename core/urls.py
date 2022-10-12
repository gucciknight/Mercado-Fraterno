from django.urls import include, path

from .views import market 

urlpatterns = [
    path('', market.home, name='home'),
    path('monedas/', include(([
        path('', market.CoinListView.as_view(), name='coin_list'),
    ], 'core'), namespace='students')),
]