from rest_framework import serializers
from .models import CustomCategory, Category
from django.db.models import ForeignKey
from sujal.models import CustomUser

class CustomCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(max_length=255)
    category_icon = serializers.CharField(max_length=255)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CustomCategory
        fields = ['id','category_name', 'category_icon', 'user']

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(max_length=255)
    category_icon = serializers.CharField(max_length=255)

    class Meta:
        model = Category
        fields = ['id','category_name', 'category_icon']

    
