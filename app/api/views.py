from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from albums.models import Album
from artists.models import Artist
from songs.models import Song
from rest_framework.decorators import api_view
from .serializers import AlbumSerializer, ArtistSerializer, SongSerializer

# Create your views here.

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
        artist_data = JSONParser().parse(request)
        artist_serializer = ArtistSerializer(data=artist_data)
        if artist_serializer.is_valid():
            artist_serializer.save()
            return JsonResponse(artist_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(artist_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Artist.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Artists were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def Song_api(request):
    if request.method == 'GET':
        songs = Song.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            songs = songs.filter(name__icontains=name)

        song_serializer = SongSerializer(songs, many=True)
        return JsonResponse(song_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        song_data = JSONParser().parse(request)
        song_serializer = SongSerializer(data=song_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse(song_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(song_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Song.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Songs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def Album_api(request):
    if request.method == 'GET':
        albums = Album.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            albums = albums.filter(name__icontains=name)

        album_serializer = AlbumSerializer(albums, many=True)
        return JsonResponse(album_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        album_data = JSONParser().parse(request)
        album_serializer = AlbumSerializer(data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse(album_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(album_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Album.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Albums were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)