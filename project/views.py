from django.shortcuts import render, redirect ,HttpResponse
from app.emailbackend import emailbackend
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages




# Create your views here.
def index(request):
    return render(request,'index.html')



def dologin(request):
    if request.method == "POST":
        user = emailbackend.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
        
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')
            elif user_type == '2':
                return redirect('superuser_home2')
            elif user_type == '3':
                return redirect('basicuser_home3')
            elif user_type == '4':
                return redirect('user_home4')
            
            else:
                messages.error(request,'Email and Password are invalid !')
                return redirect('login')
            
        else:
            messages.error(request,'Email and Password are invalid !')
            return redirect('login')
            
def dologout(request):
    logout(request)
    return redirect('login') 
