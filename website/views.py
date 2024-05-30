from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post, Comments

from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

from django.http import HttpResponse

# Create your views here.
def index_view(request, **kwargs):
    context = {'Name': 'Behzad',  'Profile':'Internship', 'Phone': '+98 914 346 5560','Email': 'behzad.Abbasy@gmail.com' ,
               'About' : 'I am a PhD candidate with extensive experience in machine learning, deep learning, reinforcement learning,'
                    'image processing, machine vision, natural language processing, and optimization/metaheuristic algorithms,'
                    'including evolutionary computation and swarm intelligence. I have experience developing Machine learning'
                    'algorithms using Python and popular libraries such as PyTorch, TensorFlow, Keras, OpenCV, NLTK, Scikit-learn,'
                    'and etc.' }
    return render(request, 'website/index.html', context)