

from django.shortcuts import render
from .forms import *
from .models import *
from django.http import *
# Create your views here.

def index(request):
    
    if request.method=='POST':
        form = Myfirstform(request.POST)
        if form.is_valid():
            #True
            d = form.cleaned_data
            #print(d)
            fname = d['fname']
            lname = d['lname']
            address = d['address']
            email = d['email']
            age = d['age']

            p = Profile(fname=fname,lname=lname,email=email,address=address,
                        age=age)
            p.save()

            return HttpResponseRedirect('/')
        
    else:
        form = Myfirstform()
    return render(request,'home.html',{'form':form})




