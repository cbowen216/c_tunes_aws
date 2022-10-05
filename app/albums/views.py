from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Album
from songs.models import Song
from .forms import AlbumForm

def albumhome(request):
    return render(request, 'albums/home.html')

def albumlist(request):
    p = Paginator(Album.objects.all().order_by('artist_id__name', 'year_released'), 10)
    page = request.GET.get('page')
    albums = p.get_page(page)
    context = {
        'albums': albums
    }
    return render(request,'albums/list.html', context)

def albumview(request, pk):
    p = Paginator(Song.objects.filter(album_id=pk).order_by('disc_number', 'track_number'), 10)
    page = request.GET.get('page')
    songs = p.get_page(page)
    context = {
        'album': Album.objects.get(id=pk), 'songs': songs
    }
    return render(request,'albums/view.html', context)


@login_required
def albumadd(request):
    form = AlbumForm()
    
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        
        if form.is_valid():
            form.save()

            messages.success(request, f'New Album created!')
            return redirect('/albums/list/')

    context = {'form':form}
    return render(request, 'Albums/add.html', context)

@login_required
def albumupdate(request, pk):
    album = Album.objects.get(id=pk)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
    
        if form.is_valid():
            form.save()

            messages.success(request, f'Album updated!')
            return redirect('/albums/list/')
    else:
        
        form = AlbumForm(instance=album)

    context = {'form':form}
    return render(request, 'albums/update.html', context)

@login_required
def albumdelete(request, pk):
    album = Album.objects.get(id=pk)

    if request.method == 'POST':
        album.delete()

        messages.success(request, f'Album {album.title} deleted!')
        return redirect('/albums/list/')

    context = {'album':album}
    return render(request, 'albums/delete.html', context)