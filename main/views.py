from django.shortcuts import render
from main.models import *
from django.core.mail import send_mail, BadHeaderError
from random import random
from django.http import FileResponse, Http404


def get_area_name(name):
    dict = {
        'CK': ['Черкаська область', 'Cherkasy Oblast'],
        'CH': ['Чернігівська область', 'Chernihiv Oblast'],
        'CV': ['Черівецька  область', 'Chernivtsi Oblast'],
        'DP': ['Дніпропетровська область', 'Dnipropetrovsk Oblast'],
        'DT': ['Донецька область', 'Donetsk Oblast'],
        'IF': ['Івано-Франківська область', 'Ivano-Frankivsk Oblast'],
        'KK': ['Харківська область', 'Kharkiv Oblast'],
        'KS': ['Херсонська область', 'Kherson Oblast'],
        'KM': ['Хмельницька область', 'Khmelnytskyi Oblast'],
        'KV': ['Київська область', 'Kiev Oblast'],
        'KC': ['Київ', 'Kiev'],
        'KH': ['Кіровоградська область', 'Kirovohrad Oblast'],
        'LH': ['Луганська область', 'Luhansk Oblast'],
        'LV': ['Львівська область', 'Lviv Oblast'],
        'MY': ['Миколаївська область', 'Mykolaiv Oblast'],
        'OD': ['Одеська область', 'Odessa Oblast'],
        'PL': ['Полтавська область', 'Poltava Oblast'],
        'RV': ['Рівнинська область', 'Rivne Oblast'],
        'SM': ['Сумська область', 'Sumy Oblast'],
        'TP': ['Тернопільська область', 'Ternopil Oblast'],
        'VI': ['Вінницька область', 'Vinnytsia Oblast'],
        'VO': ['Волинська область', 'Volyn Oblast'],
        'ZK': ['Закарпатська область', 'Zakarpattia Oblast'],
        'ZP': ['Запорізька область', 'Zaporizhia Oblast'],
        'ZT': ['Житомирська область', 'Zhytomyr Oblast'],
        'CR': ['АР Крим', 'Crimea'],
        'SV': ['Севастополь', 'Sevastopol'],
    }

    return dict[name]


def get_nav_items(ctx):
    nav_events = Event.objects.all().order_by('-date')[0:3]
    nav_projects = Project.objects.all().order_by('power')[0:3]
    nav_equipment = Equipment.objects.all()[0:3]

    temp = {
        'nav_events': nav_events,
        'nav_projects': nav_projects,
        'nav_equipment': nav_equipment,
    }

    print(temp)

    ctx.update(temp)


# Create your views here.
def index(request):

    # fname = request.POST.get('name', '')
    # number = request.POST.get('number', '')
    # subject = request.POST.get('org', '')
    # message = request.POST.get('text', '')
    # from_email = request.POST.get('email', '')
    # messages = 'Name: {}\n  Number: {}\n{} \n\nFrom {}'.format(fname, number, message, from_email)
    # send_mail(subject, messages, 'noreply@ecad.energy', ['fexumiremo@easymail.top'],
    #           fail_silently=False)

    # posts = (Post.objects.all().union(Event.objects.all()).order_by('-date'))
    posts = Post.objects.all().order_by('-date')
    sliders = Slider.objects.all()
    events = Event.objects.all().order_by('-date')
    partners = Partner.objects.all()

    try:
        big_post = events[0]
    except IndexError:
        big_post = None
    small_post = posts[0:4]
    nav_items = events[0:3]

    partners = Partner.objects.all()
    ctx = {
        'big': big_post,
        'small': small_post,
        'sliders': sliders,
        'partners': partners,
    }

    get_nav_items(ctx)
    return render(request, 'index.html', ctx)


def projects(request):
    projects = Project.objects.all().order_by('-date')
    ctx = {
        'projects': projects
    }
    get_nav_items(ctx)
    return render(request, 'projects.html', ctx)


def project(request, id):
    project = Project.objects.get(pk=id)
    gallery = Photo.objects.filter(project=project)
    ctx = {
        'project': project,
        'gallery': gallery,
    }
    get_nav_items(ctx)
    return render(request, 'project_post.html', ctx)


def equipment(request):
    equipment = Equipment.objects.all()

    ctx = {'equipment': equipment}
    get_nav_items(ctx)
    return render(request, 'equipment.html', ctx)


def equipment_post(request):
    ctx = {}
    get_nav_items(ctx)
    return render(request, 'equipment_post.html', ctx)


def about(request):
    ctx = {}
    get_nav_items(ctx)
    return render(request, 'about.html', ctx)


def normbase(request):
    ctx = {}
    get_nav_items(ctx)
    return render(request, 'normbase.html', ctx)


def docs(request):
    docs = Document.objects.all()
    ctx = {
        'docs': docs
    }
    get_nav_items(ctx)
    return render(request, 'docs.html', ctx)


def events(request):
    events = Event.objects.all().order_by('-date')
    ctx = {
        'events': events
    }
    get_nav_items(ctx)
    return render(request, 'events.html', ctx)


def event(request, id):
    event = Event.objects.get(pk=id)
    ctx = {
        'event': event,
    }
    get_nav_items(ctx)
    return render(request, 'event_post.html', ctx)


def blog(request):
    post = Post.objects.all().order_by('-date')
    ctx = {
        'posts': post
    }
    get_nav_items(ctx)
    return render(request, 'blog.html', ctx)


def blogpost(request, id):
    post = Post.objects.get(pk=id)
    ctx = {
        'post': post,
    }
    get_nav_items(ctx)
    return render(request, 'blog_post.html', ctx)


def map_project(request, ar, lang):
    projects = Project.objects.filter(area=ar)
    if lang == 'uk-uk':
        area_name = get_area_name(ar)[0]
    else:
        area_name = get_area_name(ar)[1]

    sum = 0
    for prj in projects:
        sum += prj.power

    ctx = {'projects': projects,
           'power': sum,
           'area_name': area_name}
    get_nav_items(ctx)
    return render(request, 'map_projects.html', ctx)


def pdf_view(request, id):

    doc = Document.objects.filter(pk=id)[0]

    try:
        return FileResponse(open(doc.document.path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
