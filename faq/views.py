from django.http import HttpResponse
from faq.models import *
from django.views.generic.simple import direct_to_template

def index(request):
    questions = Question.objects.all()

    return direct_to_template(request, 'index.html', { 'questions' : questions})