from django.views.generic import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm


class CustomUserCreationView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'home.html'