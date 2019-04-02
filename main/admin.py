from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Post, Event, Project, Slider, Partner


class PostAdmin(TabbedTranslationAdmin):
    pass


class MapProjectAdmin(TabbedTranslationAdmin):
    pass


class EventAdmin(TabbedTranslationAdmin):
    pass


class ProjectAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Slider)
admin.site.register(Partner)
