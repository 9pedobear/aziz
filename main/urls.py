"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('employer/', include('employer.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employer.urls'))
]

if settings.DEBUG: # При включенном режиме дебаггинга будет работать утилита
    import debug_toolbar # <--- Вот эта
    urlpatterns = [                                      #<-\
        path('__debug__/', include(debug_toolbar.urls)), #<- - Все это
                      # подключается по документации
    ] + urlpatterns                                      #<-/
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) # Подключаем
    # наши медиа файлы