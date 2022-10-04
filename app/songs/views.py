from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Song

def songhome(request):
    return render(request, 'songs/home.html')

def songlist(request):
    p = Paginator(Song.objects.all().order_by('album_id', 'disc_number', 'track_number'), 10)
    page = request.GET.get('page')
    songs = p.get_page(page)
    context = {
        'songs': songs
    }
    return render(request,'songs/list.html', context)