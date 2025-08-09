from django.contrib import admin
from .models import MessageBoard


class MessageAdmin(admin.ModelAdmin):
    list_display = ['text', 'date_created']


admin.site.register(MessageBoard, MessageAdmin)
