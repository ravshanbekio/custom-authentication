from django.urls import path
from user.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register-view'),
    path('login/',LoginView.as_view(), name='login-view'),
    path('logout/',LogoutView.as_view(), name='logout-view'),
]