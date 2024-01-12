# Generated by Django 4.2.2 on 2024-01-12 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0026_alter_article_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, max_length=255, null=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='article',
            name='day',
            field=models.DateField(blank=True, max_length=10, null=True, verbose_name='稼働日'),
        ),
        migrations.AlterField(
            model_name='article',
            name='end',
            field=models.TimeField(blank=True, max_length=10, null=True, verbose_name='終業時間'),
        ),
        migrations.AlterField(
            model_name='article',
            name='start',
            field=models.TimeField(blank=True, max_length=10, null=True, verbose_name='始業時間'),
        ),
    ]
