from django.urls import path
from . import views

urlpatterns = [
    path('', views.songhome, name='songs-home'),
    path('list/', views.songlist, name='songs-list'),
    path('add/', views.songadd, name='song-add'),
    path('<str:pk>/', views.songview, name='song-view'),
    path('<str:pk>/update/', views.songupdate, name='song-update'),
    path('<str:pk>/delete/', views.songdelete, name='song-delete'),
]