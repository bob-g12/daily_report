from django.db import models

from django.utils import timezone
class Article(models.Model):

    class Meta(object):
        #作成されるテーブル名を指定
        db_table = 'posts'

    day = models.DateField('稼働日',blank=True, null=True)
    name = models.CharField('運転者名', max_length=20, blank=True, null=True)
    car_number = models.CharField('車両No', max_length=10, blank=True, null=True)
    weather = models.CharField('天気', max_length=5, blank=True, null=True)
    start = models.TimeField('始業時間',blank=True, null=True)	
    end = models.TimeField('終業時間',blank=True, null=True)
    oiling = models.IntegerField('給油',blank=True, null=True)
    oiling2 = models.IntegerField('給油',blank=True, null=True)
    oil = models.IntegerField('オイル',blank=True, null=True)

    text = models.CharField(verbose_name='本文', max_length=255, blank=True, null=True)
    created_at = models.DateField(verbose_name='作成日', default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.text, self.created_at, self.day, self.name, self.car_number, self.weather, self.start, self.end, self.oiling, self.oiling2, self.oil
