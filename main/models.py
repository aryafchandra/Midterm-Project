from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64,primary_key=True)
    password = models.CharField(max_length=128)
    fullname = models.CharField(max_length=60)
    DOB = models.DateField()
    email = models.EmailField()
    instagram = models.CharField(max_length=30)
    line = models.CharField(max_length=32)
    interest = models.CharField(max_length=200)
    domicile = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)

class ThreadModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

class MessageModel(models.Model):
    thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=1000)
    