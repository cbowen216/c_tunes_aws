from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Albums
from .serializers import AlbumSerializer

def artisthome(request):

    return render(request, 'albums/home.html')

def artistlist(request):
    context = {
        'albums': Albums.objects.all()
    }
    return render(request,'albums/list.html', context)