from modeltranslation.translator import register, TranslationOptions
from .models import Post, Event, Project


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'preview_text')


@register(Event)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Project)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


