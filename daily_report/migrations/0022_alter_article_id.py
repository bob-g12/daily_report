# Generated by Django 4.2.2 on 2024-01-12 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_report', '0021_alter_article_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.CharField(default='20240112125221', max_length=255, primary_key=True, serialize=False),
        ),
    ]
