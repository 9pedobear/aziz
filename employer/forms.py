from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class ApplocationCreateFrom(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['employer', 'date', 'category']
        widgets = {
            'employer': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'work': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'direction': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'education': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'cabinet': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'personal_consultation': forms.NumberInput(attrs={'class': 'form-control'}),
            'online_consultation': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration_consultation': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }