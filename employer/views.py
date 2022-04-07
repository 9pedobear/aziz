from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplocationCreateFrom, EmployerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import *
from feedback.forms import *


def register(request): # функция регистрации
    if request.method == 'POST': # Проверка запроса на пост
        form = UserCreationForm(request.POST) # присваиваем форму для данных
        if form.is_valid(): #  Проверка на валидность
            form.save() # Сохранение в базу
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password) # авторизация юзера
            login(request, user) # авторизация юзера
            return redirect('/') # переадресация на главную страничку
    else: # если это запрос не пост
        form = UserCreationForm() # Присваивание форму
    context = {'form': form} # контекст для передачи данных для шаблона
    return render(request, 'employer/register.html', context)# отправляем данные в шаблон



def applicationscreate(request): # Функция для создания заявки
    if str(request.user) == 'AnonymousUser': # проверка на не авторизованного юзера
        return redirect('/register') # переадресация на форму регистрации
    form = ApplocationCreateFrom(request.POST) # передача формы для данных
    if request.method == 'POST': # проверка на запрос пост
        if form.is_valid(): # проверка на валидность
            das = form.save(commit=False) # пресохранения в базу данных
            das.author = request.user # передача в столбец автора авторизованного юзера
            das.save() # сохранения в базу
            return redirect('/') # переадресация на главную старничку
    context = {'form': form} # контекст для передачи данных для шаблона
    return render(request, 'application.html', context)# отправляем данные в шаблон


def index(request): # функция для главной странички
    form = FeedbackForm() # передача формы для обратной связи
    if request.method == 'POST': # проверка на запрос пост
        form = FeedbackForm(request.POST) # передача данных на форму
        if form.is_valid(): # проверка на валидность
            das = form.save(commit=False) # пресохранение в базу
            das.author = request.user # передача автора авторизованного юзера
            das.save() # сохранение
    employer = Employer.objects.all() # передача в переменную все обьекты из базы специалистов
    category = Category.objects.all() # передача в переменнуб все обьекты из базы категории
    sliders = Slider.objects.all() # передача в переменную все обьекты из базы слайды
    return render(request, 'index.html', {  'employers': employer,
                                            'categories': category,
                                            'form': form,
                                            'sliders': sliders})# отправляем данные в шаблон


@login_required() # декоратор проверки на авторизонного человека
def applications_edit(request, pk): # функция на редактирования заявки
    application = get_object_or_404(Application, pk=pk) # поиск определенной заявки
    if request.method == "POST": # проверка на запрос пост
        form = ApplocationCreateFrom(request.POST, instance=application) # перердача данных формы
        if form.is_valid(): # проверка на валидность
            form.save() # сохранение в базу
            return redirect('/') # переадресация на главную страницу
    else:
        form = ApplocationCreateFrom(instance=application)  # передача данных через форму
    return render(request, 'edit_do.html', {'form': form})# отправляем данные в шаблон

@login_required() # проверка на авторизованного человека
def employer_edit(request, pk): # функция для редактирования специалистов
    employer = get_object_or_404(Employer, pk=pk) # поиск определенного специалиста
    if request.method == "POST": # проверка на запрос пост
        form = EmployerForm(request.POST, instance=employer)
        if form.is_valid(): # проверка на валидность
            employer = form.save(commit=False) # пресохранения в базу
            employer.author = request.user # присваиванния автора
            employer.save()  # сохранения в базу
            return redirect('/', pk=employer.pk) # переадресация на главную старницу
    else:
        form = EmployerForm(instance=employer) # инче оставляем форму
    return render(request, 'employer_edit.html', {'form': form}) # отправляем данные в шаблон


def employers(request): # функция для покааза специалистов
    employers = Employer.objects.all() # передача в переменную все обьекты из базы специалистов
    return render(request, 'employer/employers.html', {'employers': employers})# отправляем данные в шаблон


def applicationlist(request): # функция для просмотра своих заявок
    applications = Application.objects.filter(author=request.user.pk)  # передача в переменную отфильтрованные по айди юзера обьекты из базы специалистов
    return render(request, 'employer/applicationlist.html', {'applications': applications})# отправляем данные в шаблон


def feedbacks(request): # функция для просмотра всех отзывов
    feedbacks = Feedback.objects.all() # передача в переменную все обьекты из базы
    return render(request, 'feedbacks.html', {'feedbacks': feedbacks})# отправляем данные в шаблон


def employer_detail(request, pk): # функция для просмотра сотрудника
    employers = Employer.objects.get(id=pk) # получаем конкретного сотрудника
    return render(request, 'epmloyer_detail.html', {'employer': employers})# отправляем данные в шаблон
