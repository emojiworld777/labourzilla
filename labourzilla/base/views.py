from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def user_login(request):
    return render(request, 'login.html')

def user_signup(request):
    return render(request, 'signUp.html')

def job_list(request):
    return render(request, 'jobs.html')

def howitworks(request):
    return render(request,'howItWorks.html')

def postproject(request):
    return render(request, 'postProject.html')