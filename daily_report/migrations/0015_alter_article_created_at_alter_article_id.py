# Generated by Django 4.2.2 on 2024-01-11 23:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0014_alter_article_car_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]
