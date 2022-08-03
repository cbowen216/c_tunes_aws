from django.shortcuts import render
from django.http import HttpResponse

dmyartist = [
    {
        'id': 1,
        'name': 'Pink Floyd'
    },
    {
        'id': 2,
        'name': 'Pink'
    },
    {
        'id': 3,
        'name': 'Metallica'
    }
]

def artisthome(request):

    return render(request, 'artists/home.html')

def artistlist(request):
    context = {
        'artists': dmyartist
    }
    return render(request,'artists/list.html', context)
