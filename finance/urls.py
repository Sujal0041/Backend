from django.urls import path
from .views import TransactionCreateView, get_all_transactions, WalletListCreateView, get_all_wallets

urlpatterns = [
    path('transaction/add/', TransactionCreateView.as_view(), name='add_transaction'),
    path('transactions/', get_all_transactions, name='transaction_list'),
    path('wallet/add/', WalletListCreateView.as_view(), name='add_wallet'),
    path('wallets/', get_all_wallets, name='wallet_list'),
]