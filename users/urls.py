from django.urls import path

from .views import CustomUserCreationView, SuccessView

urlpatterns = [
    path('home/', CustomUserCreationView.as_view(), name='home'),
    path('success/', SuccessView.as_view(), name='success')
]