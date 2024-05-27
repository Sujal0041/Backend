from rest_framework import serializers
from .models import FinanceTransaction, Wallet
from category.serializers import CustomCategorySerializer, CategorySerializer
from goals.serializers import GoalSerializer

class FinanceTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceTransaction
        fields = '__all__'

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class AllTransaction(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    custom = CustomCategorySerializer(read_only=True)
    goal = GoalSerializer(read_only=True)
    wallet = WalletSerializer(read_only=True)

    class Meta:
        model = FinanceTransaction
        fields = ['id', 'amount', 'type', 'notes', 'date', 'category', 'custom', 'goal', 'wallet', 'user']