from rest_framework import serializers

from accounts.models import User
from data.models import Genre, Artist, Song, Cuisine, Food, SportType, Sport, Movie, \
    HobbyType, Hobby, TvShow, Actor, Album


class MusicGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(
        # Slug related to display a field in the response
        # instead of showing the id of that foreign key
        queryset=Artist.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(
        # Slug related to display a field in the response
        # instead of showing the id of that foreign key
        queryset=Artist.objects.all(),
        slug_field='name'
    )

    album = serializers.SlugRelatedField(
        # Slug related to display a field in the response
        # instead of showing the id of that foreign key
        queryset=Album.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Song
        fields = '__all__'


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    cuisine = serializers.SlugRelatedField(
        # Slug related to display a field in the response
        # instead of showing the id of that foreign key
        queryset=Cuisine.objects.all(),
        slug_field='name'
    )
    user = serializers.SlugRelatedField(
        # Slug related to display a field in the response
        # instead of showing the id of that foreign key
        many=True,
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Food
        fields = '__all__'


class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = '__all__'


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        # Slug related to display a field in the response
        # instead of showing the id of that foreign key
        many=True,
        queryset=Genre.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class TvShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TvShow
        fields = '__all__'


class HobbyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HobbyType
        fields = '__all__'


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
