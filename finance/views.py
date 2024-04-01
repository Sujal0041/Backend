from django.views.generic.edit import CreateView
from .models import FinanceTransaction, Wallet
from django.http import JsonResponse
from .serializers import FinanceTransactionSerializer, WalletSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics

class TransactionCreateView(APIView):
    def post(self, request):
        serializer = FinanceTransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()
            # Update wallet amount based on transaction type
            wallet = transaction.wallet
            if transaction.type == 'income':
                wallet.amount += transaction.amount
            elif transaction.type == 'expense':
                wallet.amount -= transaction.amount
            wallet.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def get_all_transactions(request):
    transactions = FinanceTransaction.objects.all()
    serializer = FinanceTransactionSerializer(transactions, many=True)
    return JsonResponse(serializer.data, safe=False)

class WalletListCreateView(APIView):
    def post(self, request):
        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_all_wallets(request):
    wallets = Wallet.objects.all()
    serializer = WalletSerializer(wallets, many=True)
    return JsonResponse(serializer.data, safe=False)