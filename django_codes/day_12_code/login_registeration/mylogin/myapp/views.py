from django.shortcuts import render,redirect
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
# Create your views here.

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
    return render(request,'index.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

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
            
            return HttpResponseRedirect('/')
        
    else:
        form = Myform()
    return render(request,'form.html')















    
