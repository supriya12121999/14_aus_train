
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout

def user_login(request):
    return render(request,'login.html')

def user_auth(request):
    if request.method=='POST':
        u = request.POST.get('uname',None)
        p = request.POST.get('psw',None)
        #print(p)
        user = authenticate(username=u, password=p)
        #print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Invalid username or password')
        
def index(request):
    data = Post.objects.all()
    return render(request,'home.html',{'d':data})

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    if request.user.is_authenticated:
        return index(request)
    else:
        return user_login(request)
    
def detail(request,d):
    info = Post.objects.get(id=d)  #d=4
    return render(request,'detail.html',{'record':info})

def myform(request):
    if request.method=='POST':
        form = Postform(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            #
            f.author = request.user
            f.save()
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

def Register_Form(request):
    if request.method=='POST':
        form = Myform(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            fname = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']

            User.objects.create_user(username=uname,
                                     first_name=fname,
                                     email = email,
                                     password = pwd)
            
            return redirect('home')
        
    else:
        form = Myform()
    return render(request,'reg_form.html')



    



    













