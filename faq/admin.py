__author__ = 'oim'

from faq.models import Question
from faq.models import Answer
from faq.models import Tag

from django.contrib import admin


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class TagsInLine(admin.TabularInline):
    model = Question.tags.through
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'author_name', 'author_email', 'created']
    fields = ['question_text', 'author_name', 'author_email', 'created']
    inlines = [TagsInLine, AnswerInline]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Tag)