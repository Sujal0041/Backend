from django.shortcuts import render
from rest_framework import generics
from .models import Category, CustomCategory
from .serializers import CategorySerializer, CustomCategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from goals.models import Goal
from goals.serializers import GoalSerializer
from collections import OrderedDict
from rest_framework import serializers


class CategoryListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        custom_categories = CustomCategory.objects.filter(user=request.user)
        categories = Category.objects.exclude(category_name='Goals')
        
        custom_serializer = CustomCategorySerializer(custom_categories, many=True)
        category_serializer = CategorySerializer(categories, many=True)

        latest_category_id = Category.objects.latest('id').id

        combined_data = category_serializer.data + [
            OrderedDict([
                ('id', latest_category_id + index + 1), 
                ('category_name', goal['category_name']),
                ('category_icon', goal['category_icon'])
            ]) for index, goal in enumerate(custom_serializer.data)
        ]

        return Response(combined_data, status=status.HTTP_200_OK)

    
    def get_queryset(self):
        queryset = Category.objects.exclude(category_name='Goals')
        return queryset

    def get_serializer_class(self):
        return CategorySerializer

class CategoryListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        categories = Category.objects.all()

        category_serializer = CategorySerializer(categories, many=True)

        return Response(category_serializer.data, status=status.HTTP_200_OK)

class CustomCategoryList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        custom_categories = CustomCategory.objects.filter(user=request.user)
        custom_serializer = CustomCategorySerializer(custom_categories, many=True)
        return Response(custom_serializer.data, status=status.HTTP_200_OK)


class CustomCategoryListCreate(generics.ListCreateAPIView):
    queryset = CustomCategory.objects.all()
    serializer_class = CustomCategorySerializer


class CategoryGoalView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access

    def get(self, request):
        # Filter CustomCategory instances by the currently logged-in user
        custom_categories = CustomCategory.objects.filter(user=request.user)

        categories = Category.objects.all()
        goals = Goal.objects.all()
        
        custom_serializer = CustomCategorySerializer(custom_categories, many=True)
        category_serializer = CategorySerializer(categories, many=True)
        
        category_data = category_serializer.data
        custom_category_data = custom_serializer.data

        category_data = [cat for cat in category_data if cat['category_name'] != 'Goals']
        
        goal_serializer = GoalSerializer(goals, many=True)
        goal_data = goal_serializer.data

        latest_category_id = Category.objects.latest('id').id
        
        combined_data =  category_data + custom_category_data +[
            OrderedDict([
                ('id', latest_category_id + index + 1), 
                ('category_name', goal['name']),
                ('category_icon', 'flag-checkered')
            ]) for index, goal in enumerate(goal_data)
        ]

        return Response(combined_data, status=status.HTTP_200_OK)


class CustomCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomCategory.objects.all()
    serializer_class = CustomCategorySerializer
    lookup_field = 'pk'

class CustomCategoryCreate(generics.CreateAPIView):
    queryset = CustomCategory.objects.all()
    serializer_class = CustomCategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
