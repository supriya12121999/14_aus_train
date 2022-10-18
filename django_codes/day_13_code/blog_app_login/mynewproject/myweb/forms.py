
from django import forms
from .models import *
from django.contrib.auth.models import User

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']


class Myform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','email','password']








    








    







    
