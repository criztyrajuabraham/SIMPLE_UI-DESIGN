

from django.urls import path

from myapp import views


urlpatterns = [

    path("", views.home, name="home"),
    path('index',views.index,name='index'),
    path('login',views.login_url,name='login_url'),

    
]