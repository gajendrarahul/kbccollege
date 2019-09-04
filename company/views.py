from django.shortcuts import render, redirect
from .form import companyForm

# Create your views here.
def create(request):
    if request.method == "GET":

        context ={
            'form': companyForm()
        }
        return render(request, 'company_create.html', context)
    else:
        form = companyForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id #currently logedin user id
            data.save()
            return redirect('company_dashboard')
        else:
            return render(request, 'company_create.html', {'form': form})
