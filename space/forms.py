from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    first_name=forms.CharField( widget=forms.TextInput(attrs={'class': 'register-control', 'placeholder': 'First Name'}))
    last_name=forms.CharField( widget=forms.TextInput(attrs={'class': 'register-control', 'placeholder': 'Last Name'}))
    username=forms.CharField( widget=forms.TextInput(attrs={'class': 'register-control', 'placeholder': 'Username'}))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class': 'register-control', 'placeholder': 'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-control', 'placeholder': 'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'register-control', 'placeholder': 'Repeat password'}))

    class Meta:
        model= User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'register-control'}),
            'last_name': forms.TextInput(attrs={'class': 'register-control'}),
            'username': forms.TextInput(attrs={'class': 'register-control'}),
            'email': forms.EmailInput(attrs={'class': 'register-control'}), 
            'password1': forms.PasswordInput(attrs={'class': 'register-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'register-control'})
        }
        
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'login-control', 'placeholder': 'Enter username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login-control', 'placeholder': 'Enter password'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            
        }

class CreateTitleForm(forms.Form):
    title=forms.CharField(label='', max_length=250, widget=forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Create post...'}))

class CreatePostForm(forms.Form):
    title=forms.CharField(label='Title', max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image =forms.ImageField(label='Image', widget=forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}), required=False)
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10}), required=False)
    tags =forms.ModelMultipleChoiceField(label='Tags', queryset=Tag.objects.all(), required=False)
    

