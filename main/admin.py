from django.contrib import admin

from .models import MapProject, Post, Event, Project

admin.site.register(Post)
admin.site.register(MapProject)
admin.site.register(Event)
admin.site.register(Project)
