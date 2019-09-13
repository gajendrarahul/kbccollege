from django.shortcuts import render, redirect
from .form import jobseekerForm
from jobseeker .form import skillForm
from . models import Jobseeker,Skill

# Create your views here.
def create(request):
    if request.method == "GET":

        context ={
            'form': jobseekerForm()
        }
        return render(request, 'jobseeker_create.html',context)
    else:
        form = jobseekerForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id #currently logedin user id
            data.save()
            return redirect('dashboard')
        else:
            return render(request, 'jobseeker_create.html', {'form': form})

def skill_store(request):
    if request.method=="GET":
        return redirect('dashboard')
    else:
        form = skillForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            a = Jobseeker.objects.get(user_id=request.user.id)
            data.jobseeker_id = a.id
            data.save()
            return redirect('dashboard')
        else:
            return redirect('dashboard')

def remove(request,x):
    s=Skill.objects.get(id=x)
    s.delete()
    return  redirect('dashboard')
