from django import forms
from django.db import models
from .models import User


class InterestForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["fullname", "DOB","domicile", "gender", "line", "instagram", "email"]

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "username", "password"]

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='password', max_length=128)