from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import signupForm
from jobseeker.models import Jobseeker,Project,Skill
from company.models import Comapany
from django.contrib.auth.models import User
from jobseeker.form import JobseekerProjectForm,skillForm
def signup(request):
    if request.method == 'GET':
        context = {
            'form': signupForm(),
                }
        return render(request, 'signup.html', context)
    else:
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your account is successfully created')
            return redirect('signin')
        else:
           return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        u = request.POST.get('username')
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            id = request.user.id
            x = checkcompanyorjobseemker(id)
            if x == 1:
                return redirect('dashboard')
            elif x == 2:
                return redirect('company_dashboard')
            else:
                return  redirect('who')

        else:
            messages.error(request, 'Ente the valid username and password')
            return redirect('signin')


@login_required(login_url='signin')
def dashboard(request):
    if request.method == "GET":
        a = User.objects.get(id=request.user.id)
        b = Jobseeker.objects.get(user_id=request.user.id)
        project = Project.objects.filter(Jobseeker_id=b.id)[::-1]
        skill =Skill.objects.filter(jobseeker_id=b.id)
        context = {
            'user': a,
            'jobseeker': b,
            'jobseeker_project_form': JobseekerProjectForm(),
            'project': project,
            'sform': skillForm(),
            'skill': skill,

        }
        return render(request, 'dashboard.html', context)
    else:
        form = JobseekerProjectForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            a = Jobseeker.objects.get(user_id=request.user.id)
            data.jobseeker_id = a.id
            data.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')

def signout(request):
    logout(request)
    return redirect('signin')
def company_dashboard(request):
    return render(request,'company_dashboard.html')
def who(request):
    return render(request, 'who.html')

def checkcompanyorjobseemker(id):
    try:
        a = Jobseeker.objects.get(user_id=id)
        return 1
    except:
        try:
            c = Comapany.objects.get(user_id=id)
            return 2
        except:
            return 3







