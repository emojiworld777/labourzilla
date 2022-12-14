from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Public, Worker, Jobs
from django.contrib.auth.models import User
def home(request):
    return render(request, 'home.html')

def user_login(request):
    return render(request, 'login.html')

def public_signup(request):
    context = {}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            public = Public(user=user, name='Unknown', mobile=9674717240, email='swakshwar@gmail.com')
            public.save()
            request.session['alert'] = 'User added successfully'
            return redirect('home')
        else:
            context['alert'] = 'Password and Password confirmation not matched'
            print(context)
            print(request.session)
            return render(request, 'public_signUp.html', context)

    return render(request, 'public_signUp.html', context)

def job_list(request):
    return render(request, 'jobs.html')

def howitworks(request):
    return render(request,'howItWorks.html')

def postproject(request):
    return render(request, 'postProject.html')