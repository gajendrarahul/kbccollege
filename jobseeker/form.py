from django import forms
from .models import Jobseeker
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