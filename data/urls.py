from django.urls import path, include
from rest_framework import routers

from . import views
from .views import FoodViewSet, CuisineViewSet, GenreSet, ArtistSet, SongSet, CuisineSet, SportTypeSet, SportSet, \
    MovieSet, TvShowSet, HobbyTypeSet, HobbySet, ActorViewSet, AlbumViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('genre', GenreSet)
router.register('artist', ArtistSet)
router.register('song', SongSet)
router.register('album', AlbumViewSet)
router.register('cuisine', CuisineSet)
router.register('sporttype', SportTypeSet)
router.register('sport', SportSet)
router.register('movie', MovieSet)
router.register('tvshow', TvShowSet)
router.register('hobbytype', HobbyTypeSet)
router.register('hobby', HobbySet)
router.register('food', FoodViewSet)
router.register('cuisine', CuisineViewSet)
router.register('actor', ActorViewSet)

urlpatterns = [
    path('index', views.index, name='index'),
    path('data/', include(router.urls)),

]
