from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.db.models import F

from faq.models import *
from faq.forms import *

def index(request):
    
    if request.method == 'POST':
        question = Question()
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()

            # TODO: add here email sending


            return HttpResponseRedirect(reverse('faq.views.question_submited'))
    else:
        form = QuestionForm()

    # Get only questions which have at least one answer
    questions = Question.objects.exclude(answer__question__isnull=True)

    return render_to_response('index.html', {
        'form': form,
        'questions': questions,
        },
        context_instance = RequestContext(request))

def question_submited(request):
    return render_to_response('question_submited.html', context_instance = RequestContext(request))