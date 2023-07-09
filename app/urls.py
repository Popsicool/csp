
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('celeb', views.celeb, name="celeb"),
    path('today', views.today, name="today"),
]
