from django.contrib import admin

from .models import Chat, Message

# РЕГИСТРАЦИЯ МОДЕЛЕЙ
admin.site.register(Chat)
admin.site.register(Message)

