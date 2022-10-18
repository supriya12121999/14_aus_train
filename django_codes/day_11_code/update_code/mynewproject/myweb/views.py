
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
# Create your views here.

def index(request):
    data = Post.objects.all()
    return render(request,'home.html',{'d':data})

def detail(request,d):
    info = Post.objects.get(id=d)  #d=4
    return render(request,'detail.html',{'record':info})

def myform(request):
    if request.method=='POST':
        form = Postform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Postform()
    return render(request,'form.html',{'form':form})

def delete_post(request,d):
    data = Post.objects.get(id=d)
    data.delete()
    return HttpResponseRedirect('/')

def edit_post(request,d):
    data = Post.objects.get(id=d)  #d=12

    if request.method=='POST':
        form = Postform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Postform(instance=data)
    return render(request,'edit_form.html',{'form':form})





    



    













