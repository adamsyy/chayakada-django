from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def signup(request):
    if request.method=='GET':
        return render(request,'main/signup.html')
    else:
        user=User.objects.create_user(request.POST['username'],password=request.POST['password'])
        user.save()
        return render(request,'main/home.html')


def loginuser(request):
    if request.method=='GET':
        return render(request,'main/loginuser.html')
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'main/loginuser.html',{'error':"credentials does not match"})
        else:
            login(request,user)  
            return redirect('signup')
            
            
        