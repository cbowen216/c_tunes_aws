from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Artist
from .serializers import ArtistSerializer

def artisthome(request):
    return render(request, 'artists/home.html')

def artistlist(request):
    context = {
        'artists': Artist.objects.all()
    }
    return render(request,'artists/list.html', context)

def artistadd(request):
    return render(request, 'artists/add.html')

@api_view(['GET', 'POST', 'DELETE'])
def Artist_api(request):
    if request.method == 'GET':
        artists = Artist.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            artists = artists.filter(name__icontains=name)

        artists_serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(artists_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        Artist_data = JSONParser().parse(request)
        Artist_serializer = ArtistSerializer(data=Artist_data)
        if Artist_serializer.is_valid():
            Artist_serializer.save()
            return JsonResponse(Artist_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(Artist_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Artist.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Artist were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)
