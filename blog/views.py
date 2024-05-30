from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post, Comments
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def blog_single(request, pid):
    if request.method == 'POST':
        form=CommentForm(request.POST)
        print('form = ', form.data)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comment submited successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your comment didnt submit')
       
    current_time = timezone.now()
    post = get_object_or_404(Post,pk=pid, status =1 ,published_date__lte=current_time)
    post.counted_view += 1
    post.save()
    next_post = Post.objects.filter(status =1 ,published_date__lte=current_time, id__gt=pid).order_by('pk').first()
    previous_post = Post.objects.filter(status =1 ,published_date__lte=current_time, id__lt=pid).order_by('pk').last()
    
    if not post.login_require:
        comments = Comments.objects.filter(post=post.id, approved=True).order_by('-created_date')
        form = CommentForm()
        context = {
            'post': post,  
            'next_post': next_post,
            'previous_post': previous_post,
            'comments': comments,
            'form':form
            }
        
        return render (request, 'blog/blog-single.html', context)
    else:
        return HttpResponseRedirect(reverse ('accounts:login'))
    
    
def blog_category(request, cat_name):
    current_time = timezone.now()
    posts = Post.objects.filter(status =1 ,published_date__lte=current_time)
    posts = posts.filter(category__name = cat_name)
    context= {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    current_time = timezone.now()
    posts = Post.objects.filter(status =1 ,published_date__lte=current_time)
    if request.method == 'GET':
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context = {'posts': posts}
    return render (request, 'blog/blog-home.html',context)