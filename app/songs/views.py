from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Songs
from .serializers import SongSerializer

def songhome(request):
    return render(request, 'songs/home.html')

def songlist(request):
    context = {
        'songs': Songs.objects.all()
    }
    return render(request,'songs/list.html', context)