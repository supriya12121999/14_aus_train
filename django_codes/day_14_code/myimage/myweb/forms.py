from django import forms
from .models import *


class Myform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
