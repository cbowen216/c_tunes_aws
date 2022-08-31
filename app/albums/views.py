from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Album

def albumhome(request):
    return render(request, 'albums/home.html')

def albumlist(request):
    context = {
        'albums': Album.objects.all()
    }
    return render(request,'albums/list.html', context)