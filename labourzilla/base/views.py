from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Public, Worker, Jobs, Bid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request, 'login.html')

def public_signup(request):
    context = {}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            public = Public(user=user, name=name, mobile=mobile, email=email)
            public.save()
            login(request, user)
            request.session['alert'] = 'User added successfully'
            return redirect('home')
        else:
            context['alert'] = 'Password and Password confirmation not matched'
            print(context)
            print(request.session)
            return render(request, 'public_signUp.html', context)

    return render(request, 'public_signUp.html', context)

def worker_signup(request):
    context = {}
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        if password == password2:
            user = User.objects.create_user(username=username, password=password)
            public = Worker(user=user, name=name, mobile=mobile, email=email)
            public.save()
            login(request, user)
            request.session['alert'] = 'User added successfully'
            return redirect('home')
        else:
            context['alert'] = 'Password and Password confirmation not matched'
            print(context)
            print(request.session)
            return render(request, 'worker_signup.html', context)

    return render(request, 'worker_signup.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def job_list(request):
    all_jobs = Jobs.objects.all()
    context = {'all_jobs': all_jobs}
    return render(request, 'jobs.html', context)

def howitworks(request):
    return render(request,'howItWorks.html')

def postproject(request):
    curr_user = request.user
    if request.method == 'POST':
        title = request.POST['title']
        describe = request.POST['describe']
        support_file = request.FILES['file']
        min_price = request.POST['min_price']
        max_price = request.POST['max_price']
        category = request.POST['category']
        job_instance = Jobs(user=curr_user, title=title, description=describe, support_file=support_file, min_price=min_price,max_price=max_price, category=category)
        job_instance.save()
        return redirect('home')
    return render(request, 'postProject.html')

def update_account(request):
    curr_user = request.user
    context={}
    pub_get, work_get = None, None
    try:
        pub_get = Public.objects.get(user = curr_user)
    except:
        work_get = Worker.objects.get(user = curr_user)
    if pub_get == None:
        context['acc'] = work_get
        instance=work_get
    else:
        context['acc'] = pub_get
        instance = pub_get
    
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        instance.name = name
        instance.mobile = number
        instance.email = email
        instance.save()
        return redirect('home')
    return render(request, 'accounts.html', context)


def bid(request, id):
    context = {}
    curr_user = request.user
    job = Jobs.objects.get(id=id)
    context['job'] = job
    try:
        worker = Worker.objects.get(user = curr_user)
    except:
        worker = None
    if worker is None:
        return HttpResponse('<h1>Looks like you dont have a worker id, you cant bid sorry</h1>')
    
    if request.method=='POST':
        amount = request.POST['amount']
        bid_instance = Bid(worker= worker, job=job, amount=amount)
        bid_instance.save()
        return redirect('home')
    return render(request, 'bidder.html', context)

def projectlist(request):
    curr_user = request.user
    jobs = Jobs.objects.filter(user=curr_user)
    context = {}
    context['all_projects'] = jobs
    return render(request, 'projectList.html', context)

def bidlist(request, id):
    context = {}
    job = Jobs.objects.get(id=id)
    all_bids = Bid.objects.filter(job = job)
    context['all_bids'] = all_bids
    return render(request, 'bidlist.html', context)
