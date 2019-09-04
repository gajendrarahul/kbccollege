from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signupForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'username'}
    ))


    password1 =forms.CharField(widget=forms.PasswordInput(
        attrs= {'class':'form-control', 'placeholder': 'Enter Your Password1'}
    ),required=True, label='password')

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your password1',}
    ), required=True,label='password confirmation')

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your mail'}
    ))

    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'first name '}
    ))

    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Last name '}
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2', 'first_name', 'last_name']




