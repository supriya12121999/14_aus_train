from django.shortcuts import render
from .forms import *
# Create your views here.

def index(request):
    form = Myfirstform()
    return render(request,'home.html',{'form':form})



