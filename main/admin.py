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


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Slider)
admin.site.register(Partner)
admin.site.register(Document)
admin.site.register(Gallery)
admin.site.register(Equipment, EquipmentAdmin)
