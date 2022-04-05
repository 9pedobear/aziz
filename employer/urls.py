from django.urls import path
from . import views
from .views import registerPage
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.register, name='registerPage'), # регистрация
    path('login/', auth_view.LoginView.as_view(template_name='employer/login.html'), name='login'), # авторизация
    path('logout/', auth_view.LogoutView.as_view(template_name='employer/logout.html'), name='logout'), # выйти
    path('application/create/', views.applicationscreate, name='applicationcreate'), # создания заявки
    path('', views.index, name='home'), # дом
    path('application/<int:pk>', views.applications_edit, name='application_edit'), # редактирования заявки
    path('employer/<int:pk>', views.employer_edit, name='profile_edit'), # редактирования специолиста
    path('employers/', views.employers, name='employers'), # список специолистов
    path('application/list', views.applicationlist, name='applicationlist'), # список заявок
    path('feedbacks', views.feedbacks, name='feedback'), # список всех отзывов
    path('employer_detail/<int:pk>', views.employer_detail, name='employer_detail'), # список всех отзывов
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # подключения статик файлов это поможет рассматривать изображения
