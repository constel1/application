import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from api import settings


class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=250, null=False)
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )
    is_admin = models.BooleanField(
        "admin status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    REQUIRED_FIELDS = ["username", "email", "password"]
    USERNAME_FIELD = "username"


    def __str__(self):
        return self.username

class Chat(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    max_no_members = models.PositiveIntegerField(default=255000)
    created_date = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(MyUser, related_name='chats_members')
    created_by = models.ForeignKey(MyUser, on_delete
    =models.CASCADE,related_name='group_admin' )

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(
        MyUser, on_delete=models.PROTECT, related_name="message_sender"
    )
    text = models.CharField(max_length=200)
    attachment = models.ImageField()
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()



