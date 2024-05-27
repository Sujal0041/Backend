from django.urls import path
from .views import TransactionCreateView, GetAllTransactionsView, WalletDeleteView, WalletListCreateView,GetAllWalletsView, TransactionUpdateView, WalletUpdateView

urlpatterns = [
    path('transaction/add/', TransactionCreateView.as_view(), name='add_transaction'),
    path('transactions/', GetAllTransactionsView.as_view(), name='transaction_list'),
    path('wallet/add/', WalletListCreateView.as_view(), name='add_wallet'),
    path('wallets/', GetAllWalletsView.as_view(), name='wallet_list'),
    path('transaction/<int:pk>/', TransactionUpdateView.as_view(), name='update_transaction'),
    path('wallet/delete/<int:pk>/', WalletDeleteView.as_view(), name='wallet-delete'),
    path('wallets/<int:pk>/update/', WalletUpdateView.as_view(), name='wallet-update'),

]