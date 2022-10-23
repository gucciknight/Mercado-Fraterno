from django.urls import include, path

from .views import market 

urlpatterns = [
    path('', market.home, name='home'),
    path('market/', include(([
        path('<int:pk>', market.MarketView.as_view(), name='coin_list'),
        path('detail_view/<int:coin_balance_id>/', market.transference, name="detail_view"),
        path('transaction_view/<int:pk>/', market.TransactionView.as_view(), name="transaction_view")
    ], 'core'), namespace='students')),
]