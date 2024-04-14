from rest_framework import serializers
from .models import Budget
from sujal.models import CustomUser
from finance.models import Wallet

class BudgetSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    wallet = serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all())

    class Meta:
        model = Budget
        fields = ['category', 'name', 'amount', 'user', 'wallet']
