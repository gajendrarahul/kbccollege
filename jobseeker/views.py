from django.shortcuts import render, redirect
from .form import jobseekerForm

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
