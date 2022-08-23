from django.urls import path
from . import views

urlpatterns = [
    path('albums/list/', views.Album_api),
    path('albums/add/', views.Album_api),
    path('artists/list/', views.Artist_api),
    path('artists/add/', views.Artist_api),
    path('artists/delete_all/', views.Artist_api),
    path('songs/list/', views.Song_api),
    path('songs/add/', views.Song_api)
]