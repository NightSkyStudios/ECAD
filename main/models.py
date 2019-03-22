from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe


# Create your models here.


class MapProject(models.Model):
    CHERKASY = 'CK'
    CHERNIHIV = 'CH'
    CHERNITVTSI = 'CV'
    DNIPRO = 'DP'
    DONETSK = 'DT'
    IVANO_FRANKIVSK = 'IF'
    KHARKIV = 'KK'
    KHERSON = 'KS'
    KHMELNYTSKYI = 'KM'
    KIEV = 'KV'
    KIEV_CITY = 'KC'
    KIROVOHRAD = 'KH'
    LUHANSK = 'LH'
    LVIV = 'LV'
    MYKOLAIV = 'MY'
    ODESSA = 'OD'
    POLTAVA = 'PL'
    RIVNE = 'RV'
    SUMY = 'SM'
    TERNOPIL = 'TP'
    VINNYTSIA = 'VI'
    VOLYN = 'VO'
    ZAKARPATTIA = 'ZK'
    ZAPORIZHIA = 'ZP'
    ZHYTOMYR = 'ZT'
    CRIMEA = 'CR'
    SEVASTOPOL = 'SV'

    AREA_CHOICES = (
        (CHERKASY, 'Черкаська'),
        (CHERNIHIV, 'Чернігівська'),
        (CHERNITVTSI, 'Черівецька'),
        (DNIPRO, 'Дніпропетровська'),
        (DONETSK, 'Донецька'),
        (IVANO_FRANKIVSK, 'Івано-Франківська'),
        (KHARKIV, 'Харківська'),
        (KHERSON, 'Херсонська'),
        (KHMELNYTSKYI, 'Хмельницька'),
        (KIEV, 'Київська'),
        (KIEV_CITY, 'Київ'),
        (KIROVOHRAD, 'Кіровоградська'),
        (LUHANSK, 'Луганська'),
        (LVIV, 'Львівська'),
        (MYKOLAIV, 'Миколаївська'),
        (ODESSA, 'Одеська'),
        (POLTAVA, 'Полтавська'),
        (RIVNE, 'Рівнинська'),
        (SUMY, 'Сумська'),
        (TERNOPIL, 'Тернопільська'),
        (VINNYTSIA, 'Вінницька'),
        (VOLYN, 'Волинська'),
        (ZAKARPATTIA, 'Закарпатська'),
        (ZAPORIZHIA, 'Запорізька'),
        (ZHYTOMYR, 'Житомирська'),
        (CRIMEA, 'АР Крим'),
        (SEVASTOPOL, 'Севастополь'),
    )

    name = models.CharField(max_length=64)
    area = models.CharField(
        max_length=2,
        choices=AREA_CHOICES,
        default=VINNYTSIA,
    )
    power = models.IntegerField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    isHidden = models.BooleanField(default=False, help_text=mark_safe("Приховати публікацію"))

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='media', null=True, blank=True,
                              help_text=mark_safe("Якщо для публікації потрібна фотографія"))
    video = models.FileField(upload_to='videos', null=True, blank=True,
                             help_text=mark_safe("Якщо для публікації потрібне відео"))
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    isHidden = models.BooleanField(default=False, help_text=mark_safe("Приховати публікацію"))

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='media', null=True, blank=True,
                              help_text=mark_safe("Якщо для публікації потрібна фотографія"))
    video = models.FileField(upload_to='videos', null=True, blank=True,
                             help_text=mark_safe("Якщо для публікації потрібне відео"))
    text = models.TextField()
    power = models.IntegerField(help_text=mark_safe("Потужність"))
    date = models.DateTimeField(default=datetime.now, blank=True)
    isHidden = models.BooleanField(default=False, help_text=mark_safe("Приховати публікацію"))

    def __str__(self):
        return self.title


