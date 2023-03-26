from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('create_incident',views.create_incident,name='create_incident'),
    path('update_incident/',views.update_incident, name='update_incident'),
    path('list_incidents/', views.list_incidents,name="list_incidents"),
    path('incidents/', views.incidents,name='incidents'),
]
