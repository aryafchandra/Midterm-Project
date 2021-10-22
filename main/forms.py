from django.forms import ModelForm
from django.db import models
from .models import User

class InterestForm(ModelForm):
    class Meta:
        model = User
        fields = ["fullname", "DOB" , "domicile" , "gender" , "line" , "instagram" , "email" ]
        