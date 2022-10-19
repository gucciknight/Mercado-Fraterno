from django.urls import include, path

from .views import market 

urlpatterns = [
    path('', market.home, name='home'),
    path('market/', include(([
        path('<int:pk>', market.MarketView.as_view(), name='coin_list'),
    ], 'core'), namespace='students')),
]