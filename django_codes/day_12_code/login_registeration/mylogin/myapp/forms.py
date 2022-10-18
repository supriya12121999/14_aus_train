from django import forms
from django.contrib.auth.models import User

# Create your forms here.
class Myform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','email','password']
    
