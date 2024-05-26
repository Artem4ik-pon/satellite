from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contacts', views.contacts, name="contacts"),
    path('satellite_one', views.satellite_one, name="satellite_one"),
    path('satellite11', views.satellite11, name="satellite11"),
    path('satellite12', views.satellite12, name="satellite12"),
    path('satellite_two', views.satellite_two, name="satellite_two"),
    path('satellite21', views.satellite21, name="satellite21"),
    path('satellite22', views.satellite22, name="satellite22"),


]


