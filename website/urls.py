import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.urls import path
from website.views import *

app_name='website'

urlpatterns=[
        path('', index_view, name='index')
]