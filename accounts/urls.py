from django.urls import path , include
from . import views
urlpatterns = [
    #アカウント管理のパス
    path('',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("home",views.home,name="home"),
    path('index',include('daily_report.urls'),name='index'),
]