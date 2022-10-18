from django.shortcuts import render
from django.http import *
from .forms import *
# Create your views here.

def index(request):
    if request.method=='POST':
        form = Myform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Myform()
    return render(request,'index.html',{'form':form})

def display(request):
    data = Profile.objects.all()
    return render(request,'home.html',{'d':data})
