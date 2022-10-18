
from django import forms

class Myfirstform(forms.Form):
    fname = forms.CharField(max_length=20)
    lname = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(max_length=15)
    age = forms.IntegerField()







    





    
    

    
