# Generated by Django 4.2.2 on 2023-12-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0002_remove_comment_article_alter_article_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='code',
            field=models.TextField(blank=True, verbose_name='コード'),
        ),
    ]
