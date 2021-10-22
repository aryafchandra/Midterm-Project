from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    fullname = models.CharField(max_length=60)
    DOB = models.DateField()
    email = models.EmailField()
    image_link = models.CharField(max_length=32)
    instagram = models.CharField(max_length=30)
    line = models.CharField(max_length=32)
    interest = models.CharField(max_length=200)
    domicile = models.IntegerField(max_length=30)
    gender = models.CharField(max_length=10)
    
