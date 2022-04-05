from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name', 'question', 'phone', 'created')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    fields = ('name', 'question', 'phone')
    save_on_top = True


admin.site.register(Feedback, FeedbackAdmin)
