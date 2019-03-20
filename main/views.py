from django.shortcuts import render
from main.models import Post
from random import random

# Create your views here.

def index(request):
    return render(request, 'index.html')


def blog(request):
    post = Post.objects.all().order_by('-date')
    ctx = {
        'posts': post
    }
    return render(request, 'blog.html',ctx)
