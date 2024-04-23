from django.shortcuts import render
from budget.models import Budget
from budget.serializers import BudgetSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from finance.models import Wallet, FinanceTransaction
from finance.serializers import WalletSerializer
from budget.serializers import BudgetSerializer
from budget.models import Budget
from django.db import models
from rest_framework import permissions

class BudgetListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def post(self, request):
        try:
            data = request.data
            data.update({"user": self.request.user.id})
            serializer = BudgetSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e) 
            import traceback
            traceback.print_exc()  
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


# Helper functions to retrieve queryset and serialize it.
def get_queryset(request):
    queryset = Budget.objects.all()
    return queryset


def get_serialized_data(queryset):
    serializer = BudgetSerializer(queryset, many=True)
    return serializer.data


# Views using helper functions
class BudgetListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = get_queryset(request)
        serialized_data = get_serialized_data(queryset)
        return Response(serialized_data, status=status.HTTP_200_OK)


class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        queryset = get_queryset(request)
        obj = get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = BudgetSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        queryset = get_queryset(request)
        obj = get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = BudgetSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        queryset = get_queryset(request)
        obj = get_object_or_404(queryset, pk=kwargs['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CalculateBudgetAmount(generics.ListAPIView):
    serializer_class = None


    def get_queryset(self):
        user = self.request.user
        print(user)
        wallet_id = self.kwargs['wallet_id']
        category_id = self.kwargs['category_id']
        queryset = FinanceTransaction.objects.filter(wallet_id=wallet_id, category_id=category_id, user_id=user, type="expense")
        print("Finance",queryset)
        return queryset
    
    def list(self, request, *args, **kwargs):
        wallet_id = self.kwargs['wallet_id']
        user_id = self.request.user
        print("User",user_id)
        queryset_budget = Budget.objects.filter(wallet_id=wallet_id, user_id=user_id)
        print(queryset_budget)
        budget_amount = queryset_budget.values('amount').first()['amount']
        queryset = self.get_queryset()
        total = queryset.aggregate(models.Sum('amount'))['amount__sum'] or 0
        print(total)
        data = {total / budget_amount}
        print(data)
        return Response(data)