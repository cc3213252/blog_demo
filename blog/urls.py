__author__ = '9'

from django.conf.urls import *
from blog.views import archive

urlpatterns = patterns("",
                      url(r'^$', archive),
                      )