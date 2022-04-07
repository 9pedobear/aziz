from django import forms
from .models import *


class FeedbackForm(forms.ModelForm):# Создаем форму
    class Meta:# Дополняем класс
        model = Feedback# соединяем с моделью
        fields = ['name', 'question', 'phone']# Поля для заполнения
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),# стиль Поля
            'question': forms.Textarea(attrs={'class': 'form-control'}),# стиль Поля
            'phone': forms.TextInput(attrs={'class': 'form-control'}),# стиль Поля
        }
