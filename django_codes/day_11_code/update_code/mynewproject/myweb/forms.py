
from django import forms
from .models import *

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','text']










    








    







    
