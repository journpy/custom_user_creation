from django.views.generic import CreateView, TemplateView
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class CustomUserCreationView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'home.html'
    success_url = reverse_lazy('success')

class SuccessView(TemplateView):
    template_name = 'success.html'