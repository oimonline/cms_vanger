__author__ = 'oim'

from django.forms import ModelForm
from faq.models import *

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('created', 'tags')