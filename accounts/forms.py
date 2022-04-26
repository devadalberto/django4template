from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"
