from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class EmployerAdmin(admin.ModelAdmin): # Админка сотрудников
    list_display = ( 'id', 'name', 'city',     # Отображение полей с модели Employer
                     'description', 'experience', 'personal_consultation',
                     'online_consultation', 'duration_consultation',
                     'couple_consultation_duration', 'get_photo',
                     'created', 'updated', 'is_published')
    list_display_links = ('id', 'name') # Отображение кликабельных полей с модели Employer
    search_fields = ('name', 'city') # Поле поиска
    list_editable = ('city',) # Поле для редактирования
    list_filter = ('name', 'city')  # Поле фильтра
    fields = ('name', 'city', 'work',  # Перечисляем все поля
              'direction', 'description', 'education',
              'experience', 'cabinet', 'personal_consultation',
              'online_consultation', 'duration_consultation',
              'couple_consultation_duration', 'photo', 'get_photo',
              'is_published')
    readonly_fields = ('get_photo',) # Поле только для чтения
    save_on_top = True # Дублирование кнопок сохранения на верх

    def get_photo(self, obj): # функция для получения и отображения фото в админке
        if obj.photo: # если есть фото
            return mark_safe(f'<img src="{obj.photo.url}" width="75">') # тогда показать фото
        else: # иначе
            return '-' # поставить прочерк

    get_photo.short_description = 'Фото' # название колотки


class AdressAdmin(admin.ModelAdmin): # Админка с адресами
    list_display = ( 'id', 'cabinet') # Отображение полей с модели Adress
    list_display_links = ('id', 'cabinet') # Отображение кликабельных полей с модели Adress
    search_fields = ('cabinet',) # Поле поиска
    list_filter = ('cabinet',) # Поле фильтра
    fields = ('cabinet',) # поле
    save_on_top = True # Дублирование кнопок сохранения на верх


class EducationAdmin(admin.ModelAdmin): # Админка с образованием
    list_display = ( 'id', 'university', 'skill', 'education_date') # Отображение полей с модели Education
    list_display_links = ('id', 'university') # Отображение кликабельных полей с модели Education
    search_fields = ('university',) # Поле поиска
    list_filter = ('university',) # Поле фильтра
    fields = ('university',) # поле
    save_on_top = True # Дублирование кнопок сохранения на верх


class CategoryAdmin(admin.ModelAdmin): # Админка с категориями
    list_display = ( 'id', 'direction') # Отображение полей с модели Category
    list_display_links = ('id', 'direction') # Отображение кликабельных полей с модели Category
    search_fields = ('direction',) # Поле поиска
    list_filter = ('direction',) # Поле фильтра
    fields = ('direction',) # поле
    save_on_top = True # Дублирование кнопок сохранения на верх


class LocationAdmin(admin.ModelAdmin): # Админка с локацией
    list_display = ( 'id', 'city') # Отображение полей с модели Location
    list_display_links = ('id', 'city') # Отображение кликабельных полей с модели Location
    search_fields = ('city',) # Поле поиска
    list_filter = ('city',) # Поле фильтра
    fields = ('city',) # поле
    save_on_top = True # Дублирование кнопок сохранения на верх


class ActivityAdmin(admin.ModelAdmin): # Админка с периодом работы
    list_display = ( 'id', 'work') # Отображение полей с модели Activity
    list_display_links = ('id', 'work') # Отображение кликабельных полей с модели Activity
    search_fields = ('work',) # Поле поиска
    list_filter = ('work',) # Поле фильтра
    fields = ('work',) # поле
    save_on_top = True # Дублирование кнопок сохранения на верх

class ApplicationAdmin(admin.ModelAdmin): # Админка с заявками
    list_display = ( 'id', 'employer') # Отображение полей с модели Application
    list_display_links = ('id', 'employer') # Отображение кликабельных полей с модели Application
    search_fields = ('employer',) # Поле поиска
    list_filter = ('employer',) # Поле фильтра
    fields = ('employer',) # поле
    save_on_top = True # Дублирование кнопок сохранения на верх

class AccountAdmin(admin.ModelAdmin): # Админка с аккаунтами
    list_display = ( 'id', 'user') # Отображение полей с модели Account
    list_display_links = ('id', 'user') # Отображение кликабельных полей с модели Account
    search_fields = ('user',) # Поле поиска
    list_filter = ('user',) # Поле фильтра
    fields = ('user',) # поле
    save_on_top = True # Дублирование кнопок сохранения на верх

class SliderAdmin(admin.ModelAdmin): # Админка со слайдерами
    list_display = ( 'id', 'image') # Отображение полей с модели Slider
    list_display_links = ('id', 'image') # Отображение кликабельных полей с модели Slider
    search_fields = ('image',) # Поле поиска
    list_filter = ('image',) # Поле фильтра
    fields = ('image',) # поле
    save_on_top = True # Дублирование кнопок сохранения на верх

#Подключение моделей и настроек админки
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Adress, AdressAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Slider, SliderAdmin)

# Меняем наименование админки
admin.site.site_title = 'Управление'
admin.site.site_header = 'Управление'
