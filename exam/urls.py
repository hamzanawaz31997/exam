from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'exam'
urlpatterns = [
    path('', views.index, name='index'),
    path('albums/', views.AlbumView.as_view()),
]
