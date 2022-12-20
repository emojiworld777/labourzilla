from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def browse_job(request):
    return render(request, 'browse_job.html')

def login(request):
    return render(request, 'login.html')

def singup(request):
    return render(request, 'signup.html')

def post_job(request):
    return render(request, 'post_job.html')
