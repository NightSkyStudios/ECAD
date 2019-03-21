from django.shortcuts import render
from main.models import MapProject, Post
from random import random


def get_area_name(name):

    dict = {
        'CK': 'Черкаська',
        'CH': 'Чернігівська',
        'CV': 'Черівецька',
        'DP': 'Дніпропетровська',
        'DT': 'Донецька',
        'IF': 'Івано-Франківська',
        'KK': 'Харківська',
        'KS': 'Херсонська',
        'KM': 'Хмельницька',
        'KV': 'Київська',
        'KC': 'Київ',
        'KH': 'Кіровоградська',
        'LH': 'Луганська',
        'LV': 'Львівська',
        'MY': 'Миколаївська',
        'OD': 'Одеська',
        'PL': 'Полтавська',
        'RV': 'Рівнинська',
        'SM': 'Сумська',
        'TP': 'Тернопільська',
        'VI': 'Вінницька',
        'VO': 'Волинська',
        'ZK': 'Закарпатська',
        'ZP': 'Запорізька',
        'ZT': 'Житомирська',
        'CR': 'АР Крим',
        'SV': 'Севастополь',
    }

    return dict[name]

# Create your views here.


def index(request):

    posts = Post.objects.all().order_by('-date')
    print(posts)
    try:
        big_post = posts[0]
    except IndexError:
        big_post = None
    small_post = posts[1:5]
    ctx = {
        'big': big_post,
        'small': small_post,
    }
    return render(request, 'index.html', ctx)


def projects(request):
    return render(request, 'projects.html')


def equipment(request):
    return render(request, 'equipment.html')


def events(request):
    return render(request, 'events.html')


def blog(request):

    post = Post.objects.all().order_by('-date')
    ctx = {
        'posts': post
    }
    return render(request, 'blog.html', ctx)


def map_project(request, ar):
    projects = MapProject.objects.filter(area=ar)
    area_name = get_area_name(ar)

    sum = 0
    for prj in projects:
        sum += prj.power

    ctx = {'projects': projects,
           'power': sum,
           'area_name': area_name}

    return render(request, 'map_projects.html', ctx)

