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




class CategoryListCreate(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Category.objects.exclude(category_name='Goals')
        return queryset

    def get_serializer_class(self):
        return CategorySerializer

class CustomCategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryGoalView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        goals = Goal.objects.all()
        
        # Serialize categories
        category_serializer = CategorySerializer(categories, many=True)
        category_data = category_serializer.data

        category_data = [cat for cat in category_data if cat['category_name'] != 'Goals']
        
        
        # Serialize goals
        goal_serializer = GoalSerializer(goals, many=True)
        goal_data = goal_serializer.data

        latest_category_id = Category.objects.latest('id').id

        
        # Create combined data
        combined_data = []

        combined_data.extend(category_data)
        combined_data.extend([
            OrderedDict([
                ('id', latest_category_id + index + 1), 
                ('category_name', goal['name']),
                ('category_icon', 'flag-checkered')
            ]) for index, goal in enumerate(goal_data)
        ])
        

        print(combined_data)
        
        return Response(combined_data, status=status.HTTP_200_OK)


class CustomCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

