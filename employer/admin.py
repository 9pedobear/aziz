from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class EmployerAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'city',
                     'description', 'experience', 'personal_consultation',
                     'online_consultation', 'duration_consultation',
                     'couple_consultation_duration', 'get_photo',
                     'created', 'updated', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'city')
    list_editable = ('city',)
    list_filter = ('name', 'city')
    fields = ('name', 'city', 'work',
              'direction', 'description', 'education',
              'experience', 'cabinet', 'personal_consultation',
              'online_consultation', 'duration_consultation',
              'couple_consultation_duration', 'photo', 'get_photo',
              'is_published')
    readonly_fields = ('get_photo',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Фото'


class AdressAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'cabinet')
    list_display_links = ('id', 'cabinet')
    search_fields = ('cabinet',)
    list_filter = ('cabinet',)
    fields = ('cabinet',)
    save_on_top = True


class EducationAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'university', 'skill', 'education_date')
    list_display_links = ('id', 'university')
    search_fields = ('university',)
    list_filter = ('university',)
    fields = ('university',)
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'direction')
    list_display_links = ('id', 'direction')
    search_fields = ('direction',)
    list_filter = ('direction',)
    fields = ('direction',)
    save_on_top = True


class LocationAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'city')
    list_display_links = ('id', 'city')
    search_fields = ('city',)
    list_filter = ('city',)
    fields = ('city',)
    save_on_top = True


class ActivityAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'work')
    list_display_links = ('id', 'work')
    search_fields = ('work',)
    list_filter = ('work',)
    fields = ('work',)
    save_on_top = True


admin.site.register(Employer, EmployerAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Adress, AdressAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Account)
admin.site.register(Application)
admin.site.register(Slider)

admin.site.site_title = 'Управление'
admin.site.site_header = 'Управление'
