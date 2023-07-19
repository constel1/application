from rest_framework import serializers
from .models import *


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model = MyUser
        fields = ("username","password", "email")

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("name","created_by","members",)

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("text","timestamp","attachment","chat_id","sender",)
        ordering=['timestamp']

