from django.shortcuts import render
from .models import MessageBoard

def home(request):
    all_messages = MessageBoard.objects.all()
    return render(request, 'boards/home.html', {'all_messages': all_messages})
