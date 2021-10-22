from django.forms import ModelForm
from django.db import models
from .models import Bio

class InterestForm(ModelForm):
    class Meta:
        model = Bio
        fields = ["fullname", "DOB","domicile", "gender", "line", "instagram", "email"]
        