from django.urls import path
from . import views

urlpatterns = [
    path('', views.albumhome, name='albums-home'),
    path('list/', views.albumlist, name='albums-list'),
    path('add/', views.albumadd, name='album-add'),
    path('<str:pk>/', views.albumview, name='album-view'),
    path('<str:pk>/update/', views.albumupdate, name='album-update'),
    path('<str:pk>/delete/', views.albumdelete, name='album-delete'),
]