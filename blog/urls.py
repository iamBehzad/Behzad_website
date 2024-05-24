import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.urls import path
from website.views import *

app_name='blog'

urlpatterns=[
    #path('url address', 'view' , 'name')
    path('<int:pid>/', blog_single,name='single'),
    path('search/', blog_search,name='search'),
    #path('rss/feed/', LatestEntriesFeed()),
]