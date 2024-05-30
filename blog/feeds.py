from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post
from django.utils import timezone

class LatestEntriesFeed(Feed):
    title = "blog newst post"
    link = "/rss/feed"
    description = "best blog ever"

    def items(self):
        current_time = timezone.now()
        return Post.objects.filter(status= True,published_date__lte=current_time)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:5]