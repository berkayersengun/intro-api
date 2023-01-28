from django.http import HttpResponse
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from data.models import Food, Cuisine, Song, Artist, SportType, Sport, Genre, Movie, TvShow, Hobby, \
    HobbyType, Actor, Album
from data.serializers import FoodSerializer, CuisineSerializer, ArtistSerializer, SongSerializer, SportTypeSerializer, \
    SportSerializer, TvShowSerializer, MovieSerializer, GenreSerializer, ActorSerializer, AlbumSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class BaseModelViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    # lookup_field = 'name'


class ArtistSet(BaseModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongSet(BaseModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class CuisineSet(BaseModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer


class FoodViewSet(BaseModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class SportTypeSet(BaseModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer


class SportSet(BaseModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer


class GenreSet(BaseModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieSet(BaseModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class TvShowSet(BaseModelViewSet):
    queryset = TvShow.objects.all()
    serializer_class = TvShowSerializer


class HobbyTypeSet(BaseModelViewSet):
    queryset = HobbyType.objects.all()
    serializer_class = FoodSerializer


class HobbySet(BaseModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = FoodSerializer


class CuisineViewSet(BaseModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer


class ActorViewSet(BaseModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class AlbumViewSet(BaseModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
