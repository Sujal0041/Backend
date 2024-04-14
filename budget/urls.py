from django.urls import path
from .views import BudgetListCreateView, BudgetListView, BudgetDetailView

urlpatterns = [
    path('budget/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('budget/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
    path('budget-list/', BudgetListView.as_view(), name='budget-list'),
]
