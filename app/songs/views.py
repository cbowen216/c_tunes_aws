from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Song

def songhome(request):
    return render(request, 'songs/home.html')

def songlist(request):
    context = {
        'songs': Song.objects.all()
    }
    return render(request,'songs/list.html', context)