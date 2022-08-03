from django.urls import path
from . import views

urlpatterns = [
    path('', views.artisthome, name='artists-home'),
    path('list/', views.artistlist, name='artists-list'),
]