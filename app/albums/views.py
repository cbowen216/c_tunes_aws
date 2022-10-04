from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Album

def albumhome(request):
    return render(request, 'albums/home.html')

def albumlist(request):
    p = Paginator(Album.objects.all().order_by('artist_id', 'year_released'), 10)
    page = request.GET.get('page')
    albums = p.get_page(page)
    context = {
        'albums': albums
    }
    return render(request,'albums/list.html', context)