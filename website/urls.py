import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.urls import path
from website.views import *
from website.templatetags.website_tags import contact
from blog.feeds import LatestEntriesFeed
app_name='website'

urlpatterns=[
path('', index_view, name='index'),
path('',contact, name='contact'),
path('rss/feed/', LatestEntriesFeed()),
]
