from django.urls import path
from . import views

urlpatterns = [
    path('', views.songhome, name='songs-home'),
    path('list/', views.songlist, name='songs-list'),
]