

from django.shortcuts import render
from .forms import *
from .models import *
from django.http import *
# Create your views here.

def index(request):
    
    if request.method=='POST':
        form = Myfirstform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Myfirstform()
    return render(request,'home.html',{'form':form})









