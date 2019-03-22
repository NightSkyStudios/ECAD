from modeltranslation.translator import register, TranslationOptions
from .models import MapProject, Post, Event, Project


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Event)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Project)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(MapProject)
class PostTranslationOptions(TranslationOptions):
    fields = ('name',)

