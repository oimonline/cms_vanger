__author__ = 'oim'

from django.conf.urls.defaults import *
from faq.views import *

urlpatterns = patterns('',
    (r'^$', index),
    (r'^question_submited/$', question_submited),
    )