from django.db import models

from django.utils import timezone

import datetime
class Article(models.Model):
    def id_create():
        id_input = str(datetime.datetime.now())
        id_change = id_input.replace(" ","_")
        return id_change
    class Meta(object):
        
        #作成されるテーブル名を指定
        db_table = 'posts'
        verbose_name = 'verbose_name'
    #項目作成
    day = models.DateField('稼働日',blank=True, null=True)
    name = models.CharField('運転者名', max_length=20, blank=True, null=True)
    car_number = models.CharField('車両No', max_length=5, blank=True, null=True)
    weather = models.CharField('天気', max_length=5, blank=True, null=True)
    start = models.TimeField('始業時間',blank=True, null=True)	
    end = models.TimeField('終業時間',blank=True, null=True)
    oiling = models.FloatField('給油',max_length=4,blank=True, null=True)
    oiling2 = models.FloatField('給油',max_length=4,blank=True, null=True)
    oil = models.FloatField('オイル',max_length=4,blank=True, null=True)
    text = models.CharField(verbose_name='備考欄', max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="作成日時",default=timezone.now, blank=True, null=True)
    id = models.CharField(primary_key=True, default=id_create, editable=False, max_length=255)

    def __str__(self):
        
        return str(self.id)
