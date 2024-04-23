from django.urls import path
from .views import GoalListCreateView, GoalDetailView, CalculateGoalProgress, GoalListView

urlpatterns = [
    path('goal/', GoalListCreateView.as_view()),
    path('goal/<int:pk>/', GoalDetailView.as_view()),
    path('goal/<int:goal_id>/progress/', CalculateGoalProgress.as_view()),
    path('goal-list/', GoalListView.as_view(), name='goal-list'),

]
