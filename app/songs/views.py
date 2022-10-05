from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Song
from .forms import SongForm

def songhome(request):
    return render(request, 'songs/home.html')

def songlist(request):
    p = Paginator(Song.objects.all().order_by('artist_id__name', 'album_id__title', 'disc_number', 'track_number'), 10)
    page = request.GET.get('page')
    songs = p.get_page(page)
    context = {
        'songs': songs
    }
    return render(request,'songs/list.html', context)

def songview(request, pk):
    context = {
        'song': Song.objects.get(id=pk)
    }
    return render(request,'songs/view.html', context)

@login_required
def songadd(request):
    form = SongForm()
    
    if request.method == 'POST':
        form = SongForm(request.POST)
        
        if form.is_valid():
            form.save()

            messages.success(request, f'New Song created!')
            return redirect('/songs/list/')

    context = {'form':form}
    return render(request, 'songs/add.html', context)

@login_required
def songupdate(request, pk):
    song = Song.objects.get(id=pk)

    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
    
        if form.is_valid():
            form.save()

            messages.success(request, f'Song updated!')
            return redirect('/songs/list/')
    else:
        
        form = SongForm(instance=song)

    context = {'form':form}
    return render(request, 'songs/update.html', context)

@login_required
def songdelete(request, pk):
    song = Song.objects.get(id=pk)

    if request.method == 'POST':
        song.delete()

        messages.success(request, f'Song {song.title} deleted!')
        return redirect('/songs/list/')

    context = {'song':song}
    return render(request, 'songs/delete.html', context)