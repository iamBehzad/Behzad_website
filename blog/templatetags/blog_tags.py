from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('blog/blog-recent.html')
def latest_posts(count=6):
    current_time = timezone.now()
    latest_posts = Post.objects.filter(status =1,published_date__lte=current_time).order_by('-published_date')[:count]
    return {'latest_posts': latest_posts}