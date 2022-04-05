from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from .forms import UserRegisterForm, ApplocationCreateFrom, EmployerForm
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import *
from feedback.forms import *
# Create your views here.


# def create_post(request):
#     return render(request, 'user/create_post.html', )

# class AddPostView(CreateView):
#     model = News
#     template_name = 'user/create_post.html'
#     # form_class =
#     fields = '__all__'


def register(request): # функция регистрации
    print('da')
    if request.method == 'POST': # Проверка запроса на пост
        form = UserCreationForm(request.POST) # присваиваем форму для данных
        print('POST')
        if form.is_valid(): #  Проверка на валидность
            form.save() # Сохранение в базу
            print('VAlid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password) # авторизация юзера
            print('hz')
            login(request, user) # авторизация юзера
            return redirect('/') # переадресация на главную страничку
    else: # если это запрос не пост
        form = UserCreationForm() # Присваивание форму

    context = {'form': form} # контекст для передачи данных для шаблона
    return render(request, 'employer/register.html', context)


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'employer/register.html', context)


def applicationscreate(request): # Функция для создания заявки
    print(request.user)
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
    return render(request, 'application.html', context)


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
    return render(request, 'index.html', {'employers': employer, 'categories': category, 'form': form, 'sliders': sliders})


@login_required() # декоратор проверки на авторизонного человека
def applications_edit(request, pk): # функция на редактирования заявки
    application = get_object_or_404(Application, pk=pk) # поиск определенной заявки
    if request.method == "POST": # проверка на запрос пост
        print('das')
        form = ApplocationCreateFrom(request.POST, instance=application) # перердача данных формы
        if form.is_valid(): # проверка на валидность
            print('das')
            form.save() # сохранение в базу
            return redirect('/') # переадресация на главную страницу
    else:
        form = ApplocationCreateFrom(instance=application)  # передача данных через форму
    return render(request, 'edit_do.html', {'form': form})

@login_required() # проверка на авторизованного человека
def employer_edit(request, pk): # функция для редактирования специалистов
    print(request.user)
    employer = get_object_or_404(Employer, pk=pk) # поиск определенного специалиста
    if request.method == "POST": # проверка на запрос пост
        print('post')
        form = EmployerForm(request.POST, instance=employer)
        if form.is_valid(): # проверка на валидность
            employer = form.save(commit=False) # пресохранения в базу
            employer.author = request.user # присваиванния автора
            print('yes')
            # return HttpResponse(do)
            employer.save()  # сохранения в базу
            return redirect('/', pk=employer.pk) # переадресация на главную старницу
    else:
        form = EmployerForm(instance=employer)
    return render(request, 'employer_edit.html', {'form': form})


def employers(request): # функция для покааза специалистов
    employers = Employer.objects.all() # передача в переменную все обьекты из базы специалистов
    return render(request, 'employer/employers.html', {'employers': employers})


def applicationlist(request): # функция для просмотра своих заявок
    applications = Application.objects.filter(author=request.user.pk)  # передача в переменную отфильтрованные по айди юзера обьекты из базы специалистов
    print(applications)
    return render(request, 'employer/applicationlist.html', {'applications': applications})


def feedbacks(request): # функция для просмотра всех отзывов
    feedbacks = Feedback.objects.all() # передача в переменную все обьекты из базы
    return render(request, 'feedbacks.html', {'feedbacks': feedbacks})


def employer_detail(request, pk):
    employers = Employer.objects.get(id=pk)
    return render(request, 'epmloyer_detail.html', {'employer': employers})
