from django.urls import path
from .views import CategoryListCreate, CustomCategoryDetail, CategoryGoalView, CustomCategoryCreate, CustomCategoryList, CategoryListView
from goals.views import GoalListViewRemoved

urlpatterns = [
    path('category/', CategoryListCreate.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('category/custom/', CustomCategoryList.as_view()),
    path('category/goal/', GoalListViewRemoved.as_view()),
    path('category/<int:pk>/', CustomCategoryDetail.as_view()),
    path('category/combined/', CategoryGoalView.as_view()),
    path('category/create/', CustomCategoryCreate.as_view()),
]
