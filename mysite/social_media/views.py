from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from social_media.models import Reguserstud 
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login 


# Create your views here.
def index(request):
    return render(request,"index.html")
def singup(request):
    return render(request,"singup.html")
def login(request):
    if request.method == "POST" :
        username=request.POST.get("username")
        email=request.POST.get("Email")
        password=request.POST.get("pass1")

        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None : 
            auth_login(request,user)
            return redirect('user')
        else:
            messages.error(request,"Bad Credential")
            return redirect('singup')    
    return render(request,"login.html")
def communiity(request):
    return render(request,"communiity.html")
def courses(request):
    return render(request,"courses.html")
def intern(request):
    return render(request,"intern.html")
def project(request):
    return render(request,"project.html")
def singuprec(request):
        return render(request,"singuprec.html")
def singupteach(request):
        return render(request,"singupteach.html")
def singupstud(request):
     if request.method == "POST" : 
         first_name=request.POST.get("fname")
         last_name=request.POST.get("lname")
         uniquename=request.POST.get("User_name")
         Education_level=request.POST.get("Education_level")
         pass_user=request.POST.get("pass1")
         Email_add=request.POST.get("Email")
        
         user= User.objects.create_user(uniquename,Email_add,pass_user)
         user.save()
         Reguserstud1= Reguserstud(FirstName=first_name,  LastName=last_name,EducationLevel=Education_level
                                  , email=Email_add, password=pass_user)
         Reguserstud1.save()
         return redirect('/login')       
     return render(request,"singupstud.html")
def loginrec(request):
     return render(request,"loginrec.html")
def loginteach(request):
     return render(request,"loginteach.html")
def user(request):
     return render(request,"user.html")