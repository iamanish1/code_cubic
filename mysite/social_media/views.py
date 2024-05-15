from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def singup(request):
    return render(request,"singup.html")
def login(request):
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