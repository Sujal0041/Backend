from django.urls import path
from .views import CategoryListCreate, CustomCategoryDetail, CategoryGoalView

urlpatterns = [
    path('category/', CategoryListCreate.as_view()),
    path('category/<int:pk>/', CustomCategoryDetail.as_view()),
    path('category/combined/', CategoryGoalView.as_view()),
]
