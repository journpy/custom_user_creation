from django.urls import path

from .views import CustomUserCreationView, SuccessView

urlpatterns = [
    path('signup/', CustomUserCreationView.as_view(), name='signup'),
    path('success/', SuccessView.as_view(), name='success'),
]
