from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Artist
from albums.models import Album
from .forms import ArtistForm

def artisthome(request):
    return render(request, 'artists/home.html')

def artistlist(request):
    p = Paginator(Artist.objects.all().order_by('name'), 10) # Show 10 artists per page.
    page = request.GET.get('page')
    artists = p.get_page(page)
    context = { 'artists': artists
    }
    return render(request,'artists/list.html', context)

def artistview(request, pk):
    context = {
        'artist': Artist.objects.get(id=pk), 'albums': Album.objects.filter(artist_id=pk).order_by('year_released')
    }
    return render(request,'artists/view.html', context)

@login_required
def artistadd(request):
    form = ArtistForm()
    
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        
        if form.is_valid():
            form.save()

            messages.success(request, f'New Artist created!')
            return redirect('/artists/list/')

    context = {'form':form}
    return render(request, 'artists/add.html', context)

@login_required
def artistupdate(request, pk):
    artist = Artist.objects.get(id=pk)

    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
    
        if form.is_valid():
            form.save()

            messages.success(request, f'Artist updated!')
            return redirect('/artists/list/')
    else:
        
        form = ArtistForm(instance=artist)

    context = {'form':form}
    return render(request, 'artists/update.html', context)

@login_required
def artistdelete(request, pk):
    artist = Artist.objects.get(id=pk)

    if request.method == 'POST':
        artist.delete()

        messages.success(request, f'Artist {artist.name} deleted!')
        return redirect('/artists/list/')

    context = {'artist':artist}
    return render(request, 'artists/delete.html', context)