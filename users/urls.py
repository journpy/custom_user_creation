from django.urls import path

from .views import CustomUserCreationView

urlpatterns = [
    path('home/', CustomUserCreationView.as_view(), name='home'),
]