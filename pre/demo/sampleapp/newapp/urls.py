from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$',home),
    url(r'^register-student$',RegisterStudent)
]
