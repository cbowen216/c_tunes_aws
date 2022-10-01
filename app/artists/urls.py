from django.urls import path
from . import views

urlpatterns = [
    path('', views.artisthome, name='artists-home'),
    path('list/', views.artistlist, name='artists-list'),
    path('add/', views.artistadd, name='artist-add'),
    path('<str:pk>/', views.artistview, name='artist-view'),
    path('<str:pk>/update/', views.artistupdate, name='artist-update'),
    path('<str:pk>/delete/', views.artistdelete, name='artist-delete'),
]