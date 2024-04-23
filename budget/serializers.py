from rest_framework import serializers
from .models import Budget
from sujal.models import CustomUser
from finance.models import Wallet
from category.models import Category

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'