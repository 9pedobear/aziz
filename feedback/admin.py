from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):# Админка с адресами
    list_display = ( 'id', 'name', 'question', 'phone', 'created')# Отображение полей с модели
    list_display_links = ('id', 'name')# Отображение кликабельных полей с модели
    search_fields = ('name',)# Поле поиска
    list_filter = ('name',)# Поле фильтра
    fields = ('name', 'question', 'phone')# поле
    save_on_top = True# Дублирование кнопок сохранения на верх

#Подключение моделей и настроек админки
admin.site.register(Feedback, FeedbackAdmin)
