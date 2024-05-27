from django.urls import path
from .views import  register_user, LoginView, update_password, GetUserDataView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register_user, name='register'),
    path("update_password/", update_password, name="update_password"),
    path("get_user_data/", GetUserDataView.as_view(), name="get_user_data"),
]