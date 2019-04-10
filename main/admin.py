from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import *


class PostAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'isHidden']
    search_fields = ['title']
    list_filter = ['isHidden']


class EventAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'date', 'isHidden']
    list_filter = ['isHidden']
    search_fields = ['title']


class ProjectAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'area', 'power', 'isHidden']
    list_filter = ('area', 'isHidden')
    search_fields = ['title']



class DocumentAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'isHidden']
    list_filter = ('title', 'isHidden')

admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Slider)
admin.site.register(Partner)
admin.site.register(Document)
