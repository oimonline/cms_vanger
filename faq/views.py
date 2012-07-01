from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from faq.models import *
from faq.forms import *

def index(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question()
            question.question_text = form.cleaned_data['question_text']
            question.author_name = form.cleaned_data['author_name']
            question.author_email = form.cleaned_data['author_email']
            question.save()

            for tag in form.cleaned_data['tags']:
                question.tag_set.add(tag)


            return HttpResponseRedirect(reverse('faq.views.question_submited'))
    else:
        form = QuestionForm()

    questions = Question.objects.all()

    return render_to_response('index.html', {
        'form': form,
        'questions': questions,
        },
        context_instance = RequestContext(request))

def question_submited(request):
    return render_to_response('question_submited.html', context_instance = RequestContext(request))