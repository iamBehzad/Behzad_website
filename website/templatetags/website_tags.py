from django.shortcuts import render,get_object_or_404,redirect
from django import template
from blog.models import Post,Category
from website.models import Type,Proj_Cert
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

register = template.Library()

'''
@register.simple_tag
def function(a):
    posts = Post.objects.filter(statuse = 1)
    return posts
'''
'''
@register.filter
def snippet(value):
    return value[0:100]
'''
@register.inclusion_tag('website/projects.html', takes_context=True)
def projects(context):
    request = context.get('request')
    projects= Proj_Cert.objects.filter(type__name = 'Project').order_by('created_date')
    projects = Paginator(projects,3)
    try:
        page_number=request.GET.get('proj_page')
        projects = projects.page(page_number)
    except EmptyPage: 
        projects= projects.get_page(1)
    except PageNotAnInteger:
        projects = projects.get_page(1)
        
    return {'projects':projects}


@register.inclusion_tag('website/certificates.html', takes_context=True)
def certificates(context):
    request = context.get('request')
    certificates= Proj_Cert.objects.filter(type__name = 'Certificate').order_by('created_date')
    certificates = Paginator(certificates,3)
    try:
        page_number=request.GET.get('cert_page')
        certificates = certificates.page(page_number)
    except EmptyPage: 
        certificates= certificates.get_page(1)
    except PageNotAnInteger:
        certificates = certificates.get_page(1)
        
    return {'certificates':certificates}

@register.inclusion_tag('website/blog.html', takes_context=True)
def blog(context):
    current_time = timezone.now()
    request = context.get('request')
    if (cat:=request.GET.get('cat')):
        posts = Post.objects.filter(status =1 ,published_date__lte=current_time , category__name= cat)
    else:
        posts = Post.objects.filter(status =1 ,published_date__lte=current_time)

    posts = Paginator(posts,3)
    try:
        page_number=request.GET.get('blog_page')
        posts = posts.page(page_number)
    except EmptyPage: 
        posts= posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)

    return {'posts': posts, 'cat':cat}