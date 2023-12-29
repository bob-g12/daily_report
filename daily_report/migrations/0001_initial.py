# Generated by Django 4.2.2 on 2023-12-26 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=62, verbose_name='タイトル')),
                ('slug', models.SlugField(verbose_name='URLスラッグ（英語）')),
                ('image', models.ImageField(blank=True, help_text='登録しない場合は、デフォルトのイメージ写真を使用する', upload_to='article_image', verbose_name='記事のイメージ写真')),
                ('body', models.TextField(verbose_name='本文')),
                ('status', models.PositiveSmallIntegerField(default=1, help_text='1:下書き, 2:公開', verbose_name='公開ステータス')),
                ('liked', models.IntegerField(default=0, verbose_name='いいね数')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('creator', models.CharField(max_length=31, verbose_name='投稿者')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
            options={
                'verbose_name_plural': '記事',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, verbose_name='カテゴリ名')),
            ],
            options={
                'verbose_name_plural': 'カテゴリ',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter', models.CharField(max_length=31, verbose_name='コメント者名')),
                ('body', models.TextField(verbose_name='コメント文')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='コメント投稿日時')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='daily_report.article', verbose_name='記事')),
            ],
            options={
                'verbose_name_plural': 'コメント',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='daily_report.category', verbose_name='カテゴリ'),
        ),
    ]
