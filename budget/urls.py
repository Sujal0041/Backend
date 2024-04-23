from django.urls import path
from .views import BudgetListCreateView, BudgetListView, BudgetDetailView, CalculateBudgetAmount

urlpatterns = [
    path('budget/', BudgetListCreateView.as_view(), name='budget-list-create'),
    path('budget/<int:pk>/', BudgetDetailView.as_view(), name='budget-detail'),
    path('budget-list/', BudgetListView.as_view(), name='budget-list'),
    path('budget/<int:wallet_id>/category/<int:category_id>/total-divided-by-budget-amount/', 
        CalculateBudgetAmount.as_view(), 
        name='budget-category-total-divided-by-budget-amount'
    )
]