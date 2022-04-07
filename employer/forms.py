# импорт данных
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm): # Создаем форму
    email = forms.EmailField # Определяем поле
    class Meta: # Дополняем класс
        model = User # соединяем с моделью
        fields = ['username', 'email', 'password1', 'password2']  # Поля для заполнения
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}), # стиль Поля
            'email': forms.EmailInput(attrs={'class': 'form-control'}), # стиль Поля
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}), # стиль Поля
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}), # стиль Поля
        }


class ApplocationCreateFrom(forms.ModelForm):# Создаем форму
    class Meta:# Дополняем класс
        model = Application# соединяем с моделью
        fields = ['employer', 'date', 'category']# Поля для заполнения
        widgets = {
            'employer': forms.Select(attrs={'class': 'form-control'}), # стиль Поля
            'date': forms.SelectDateWidget(attrs={'class': 'form-control'}), # стиль Поля
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}), # стиль Поля
        }


class EmployerForm(forms.ModelForm):# Создаем форму
    class Meta:# Дополняем класс
        model = Employer# соединяем с моделью
        fields = '__all__' # Поля для заполнения
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), # стиль Поля
            'city': forms.Select(attrs={'class': 'form-control'}), # стиль Поля
            'work': forms.SelectMultiple(attrs={'class': 'form-control'}), # стиль Поля
            'direction': forms.SelectMultiple(attrs={'class': 'form-control'}), # стиль Поля
            'description': forms.Textarea(attrs={'class': 'form-control'}), # стиль Поля
            'education': forms.SelectMultiple(attrs={'class': 'form-control'}),# стиль Поля
            'experience': forms.NumberInput(attrs={'class': 'form-control'}), # стиль Поля
            'cabinet': forms.SelectMultiple(attrs={'class': 'form-control'}),# стиль Поля
            'personal_consultation': forms.NumberInput(attrs={'class': 'form-control'}),# стиль Поля
            'online_consultation': forms.NumberInput(attrs={'class': 'form-control'}),# стиль Поля
            'duration_consultation': forms.NumberInput(attrs={'class': 'form-control'}),# стиль Поля
            'photo': forms.FileInput(attrs={'class': 'form-control'}),# стиль Поля
        }