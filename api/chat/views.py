from _ast import pattern

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import MyUserSerializer, ChatSerializer, MessageSerializer


@api_view(['GET'])
def get_users(request):
    users = MyUser.objects.all()
    serializer = MyUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_user(request):
    serializer = MyUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_user(request, pk, *args, **kwargs):
    try:
        user = MyUser.objects.get(pk=pk)
    except MyUser.DoesNotExist:
        user = None
    if user is None:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MyUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_ListMessage(request, chat_id, *args, **kwargs):
    try:
        messages = Message.objects.filter(chat_id=chat_id)
    except Message.DoesNotExist:
        messages = None
    if messages is None:
        return Response({'error': 'Chat not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def get_Message(request, chat_id, message_id, *args, **kwargs):
    try:
        messages = Message.objects.filter(chat_id=chat_id)
        message = messages.get(pk=message_id)
    except Message.DoesNotExist:
        message = None
    if message is None:
        return Response({'error': 'Message not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MessageSerializer(message)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_Message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_ListChat(request):
    chats = Chat.objects.all()
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_chat(request, pk, *args, **kwargs):
    try:
        chat = Chat.objects.get(pk=pk)
    except Chat.DoesNotExist:
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    if chat is None:
        return Response({'error': 'Chat not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ChatSerializer(chat)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def post_get_chat(request, pk):
    if request.method == "GET":
        try:
            chat = Chat.objects.get(pk=pk)
        except Chat.DoesNotExist:
            serializer = ChatSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        if chat is None:
            return Response({'error': 'Chat not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ChatSerializer(chat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
