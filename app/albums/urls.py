from django.urls import path
from . import views

urlpatterns = [
    path('', views.albumhome, name='albums-home'),
    path('list/', views.albumlist, name='albums-list'),
]