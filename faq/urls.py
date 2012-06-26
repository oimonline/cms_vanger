__author__ = 'oim'

from django.conf.urls.defaults import *
from faq.views import *

urlpatterns = patterns('',
    (r'^$', default),
    )