from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64,primary_key=True)
    password = models.CharField(max_length=128)
    fullname = models.CharField(max_length=60, default='')
    DOB = models.DateField(default=timezone.now())
    email = models.EmailField(default='')
    instagram = models.CharField(max_length=30,default='')
    line = models.CharField(max_length=32,default='')
    interest = models.CharField(max_length=200,default='')
    domicile = models.CharField(max_length=30,default='')
    gender = models.CharField(max_length=10,default='')
    
    def __str__(self):
        return self.username

class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

class MessageModel(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=1000)
    