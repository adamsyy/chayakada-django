from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User, Group
from .models import Main
from .models import Todoform as todoformmodel
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer,MainSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .forms import Todoform 
# Create your views here. 

def signup(request):
    if request.method=='GET':
        return render(request,'main/signup.html')
    else:
        user=User.objects.create_user(request.POST['username'],password=request.POST['password'])
        user.save()
        main=Main.objects.all()
        return render(request,'main/home.html',{'main':main})


def loginuser(request):
    if request.method=='GET':
        return render(request,'main/loginuser.html')
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'main/loginuser.html',{'error':"credentials does not match"})
        else:
            login(request,user)  
            main=Main.objects.all()
            return render(request,'main/index.html',{'main':main})
            


def home(request):
    if request.method=='POST':
        main=Main.objects.all()
        return render(request,'main/index.html',{'main':main})
               
    if request.user.is_authenticated:
        main=Main.objects.all()
        return render(request,'main/index.html',{'main':main})
    else:
        return render(request,'main/loginuser.html')



@permission_classes((AllowAny, ))
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

@permission_classes((AllowAny, ))
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
@permission_classes((AllowAny, ))
class MainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Main.objects.all()
    serializer_class = MainSerializer
    permission_classes = [permissions.IsAuthenticated]    


def addtocart(request):
    form=Todoform(request.POST)
    newtodo=form.save(commit=False)
    newtodo.user=request.user
    newtodo.save()
    return render(request,'main/cart.html')




def cart(request):
    todos=todoformmodel.objects.filter(user=request.user)
    return render(request,'main/cart.html',{'todos':todos})




















    
