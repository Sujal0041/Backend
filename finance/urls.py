from django.urls import path
from .views import TransactionCreateView, GetAllTransactionsView, WalletListCreateView,GetAllWalletsView

urlpatterns = [
    path('transaction/add/', TransactionCreateView.as_view(), name='add_transaction'),
    path('transactions/', GetAllTransactionsView.as_view(), name='transaction_list'),
    path('wallet/add/', WalletListCreateView.as_view(), name='add_wallet'),
    path('wallets/', GetAllWalletsView.as_view(), name='wallet_list'),
]