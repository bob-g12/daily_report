# Generated by Django 4.2.2 on 2023-12-28 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0003_article_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='code',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
    ]
