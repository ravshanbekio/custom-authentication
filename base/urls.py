from django.urls import path
from base.views import DashboardView

urlpatterns = [
    path('dashboard/',DashboardView.as_view(), name='dashboard')
]