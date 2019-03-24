from django.shortcuts import render
from main.models import MapProject, Post, Event, Project, Slider
from random import random


def get_area_name(name):
    dict = {
        'CK': 'Черкаська область',
        'CH': 'Чернігівська область',
        'CV': 'Черівецька  область',
        'DP': 'Дніпропетровська область',
        'DT': 'Донецька область',
        'IF': 'Івано-Франківська область',
        'KK': 'Харківська область',
        'KS': 'Херсонська область',
        'KM': 'Хмельницька область',
        'KV': 'Київська область',
        'KC': 'Київ',
        'KH': 'Кіровоградська область',
        'LH': 'Луганська область',
        'LV': 'Львівська область',
        'MY': 'Миколаївська область',
        'OD': 'Одеська область',
        'PL': 'Полтавська область',
        'RV': 'Рівнинська область',
        'SM': 'Сумська область',
        'TP': 'Тернопільська область',
        'VI': 'Вінницька область',
        'VO': 'Волинська область',
        'ZK': 'Закарпатська область',
        'ZP': 'Запорізька область',
        'ZT': 'Житомирська область',
        'CR': 'АР Крим',
        'SV': 'Севастополь',
    }

    return dict[name]


# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-date')
    sliders = Slider.objects.all()
    try:
        big_post = posts[0]
    except IndexError:
        big_post = None
    small_post = posts[1:5]
    ctx = {
        'big': big_post,
        'small': small_post,
        'sliders': sliders
    }
    return render(request, 'index.html', ctx)


def projects(request):
    projects = Project.objects.all().order_by('-date')
    ctx = {
        'projects': projects
    }
    return render(request, 'projects.html', ctx)


def equipment(request):
    return render(request, 'equipment.html')


def events(request):
    events = Event.objects.all().order_by('-date')
    ctx = {
        'events': events
    }
    return render(request, 'events.html', ctx)


def blog(request):
    post = Post.objects.all().order_by('-date')
    ctx = {
        'posts': post
    }
    return render(request, 'blog.html', ctx)


def blogpost(request, id):
    post = Post.objects.get(pk=id)
    ctx = {
        'post': post,
    }
    return render(request, 'blog_post.html', ctx)


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
