# Generated by Django 4.2.2 on 2024-01-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0010_alter_article_start_alter_article_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='start',
            field=models.TimeField(blank=True, null=True, verbose_name='始業時間'),
        ),
    ]