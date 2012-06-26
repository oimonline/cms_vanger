__author__ = 'oim'

from faq.models import Question
from faq.models import Answer
from faq.models import Tag

from django.contrib import admin


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'created', 'tag']
    fields = ['text', 'author', 'tag', 'created']
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Tag)