from django import forms
from .models import Jobseeker, Project,Skill

class jobseekerForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    experience_year = forms.CharField(widget=forms.NumberInput(attrs={'class':'from-control'}))
    professional_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact_number =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    url = forms.URLField(widget=forms.URLInput(attrs={'class':'form-control'}))
    gender = forms.CharField(widget=forms.Select(choices=(('male','MALE'),('female','FEMALE'),('other','other'))))
    qualification =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Jobseeker
        exclude = ['user']

class JobseekerProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    link =forms.URLField(widget=forms.URLInput(attrs={'class':'form-control'}))
    class Meta:
        model = Project
        exclude = ('Jobseeker',)

class skillForm(forms.ModelForm):
    skill_title =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    proffecency_level = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Skill
        exclude = ('jobseeker',)
