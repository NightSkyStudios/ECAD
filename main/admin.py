from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import MapProject, Post, Event, Project


class PostAdmin(TabbedTranslationAdmin):
    pass


class MapProjectAdmin(TabbedTranslationAdmin):
    pass


class EventAdmin(TabbedTranslationAdmin):
    pass


class ProjectAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(MapProject, MapProjectAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Project, ProjectAdmin)
