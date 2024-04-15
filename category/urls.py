from django.urls import path
from .views import CategoryListCreate, CategoryDetail

urlpatterns = [
    path('category/', CategoryListCreate.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
]
