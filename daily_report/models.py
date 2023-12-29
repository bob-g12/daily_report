from django.db import models

class Article(models.Model):

    day = models.DateField('稼働日',blank=True, null=True)
    name = models.CharField('運転者名', max_length=20, blank=True, null=True)
    car_number = models.CharField('車両No', max_length=10, blank=True, null=True)
    weather = models.CharField('天気', max_length=5, blank=True, null=True)
    start = models.TimeField('始業時間',blank=True, null=True)	
    end = models.TimeField('終業時間',blank=True, null=True)
    oiling = models.IntegerField('給油',blank=True, null=True)
    oiling2 = models.IntegerField('給油',blank=True, null=True)
    oil = models.IntegerField('オイル',blank=True, null=True)