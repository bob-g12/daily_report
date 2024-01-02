from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),#トップページへのリンク
    path('write/', views.write, name='write'),#投稿ページへのリンク
    path('edit/<int:post_id>/',views.edit, name='edit'),
    path('review/<int:post_id>/', views.review, name='review'),
    path('exclude/<int:post_id>/', views.exclude, name='exclude'),
]
