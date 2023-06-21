from django.urls import include, path

from .views import market, administrator

urlpatterns = [
    path('', market.home, name='home'),
    path('market/', include(([
        path('<int:pk>', market.MarketView.as_view(), name='coin_list'),
        path('detail_view/<int:coin_balance_id>/', market.transference, name="detail_view"),
        path('transaction_view/<int:pk>/', market.TransactionView.as_view(), name="transaction_view"),
        path('create_coin/<int:pk>/', market.CoinCreationView.as_view(), name='create_coin'),
        path('validation_accepted/<int:transaction_id>', market.transference_validated, name='validation_accepted'),
        path('validation_denied/<int:transaction_id>', market.transference_denied, name='validation_denied'),
        path('user_validation/<int:validated_coin_balance_id>', administrator.user_validation, name='user_validation'),
        path('user_rejection/<int:unvalidated_coin_balance_id>', administrator.user_rejection, name='user_rejection'),
        path('<pk>/update', administrator.UserUpdateView.as_view(), name='user_update'),
    ], 'core'), namespace='students')),
]