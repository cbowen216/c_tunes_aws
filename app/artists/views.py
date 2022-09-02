from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from .models import Artist
from .form import NewArtistForm

def artisthome(request):
    return render(request, 'artists/home.html')

def artistlist(request):
    context = {
        'artists': Artist.objects.all()
    }
    return render(request,'artists/list.html', context)

def artistadd(request):
    context = {}
    if request.method == "POST":
        form = NewArtistForm(request.POST)

    return render(request, 'artists/add.html')