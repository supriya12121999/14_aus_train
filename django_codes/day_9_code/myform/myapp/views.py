from django.shortcuts import render
from .forms import *
from django.http import *
from .models import *
# Create your views here.

def index(request):

    if request.method == 'POST':
        form = Demoform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form  = Demoform()
        data = Demo.objects.all()
    return render(request,'home.html',{'f':form,'data':data})
