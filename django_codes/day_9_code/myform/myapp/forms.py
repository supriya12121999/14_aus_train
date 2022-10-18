from django import forms
from .models import *
# Create your models here.

class Demoform(forms.ModelForm):

    class Meta:
        model = Demo
        fields = '__all__'
    
    
