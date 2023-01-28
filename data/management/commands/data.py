import json

from django.core.management.base import BaseCommand

from data.choices import GenreType
from data.models import Sport, Genre, Movie, Actor, Cuisine, Food, Hobby, Song, Album, Artist, TvShow


def generate_genres():
    movie_genres = json.load(open('resources/data/genre/movie.json'))
    for mg in movie_genres:
        Genre.objects.create(name=mg, type=GenreType.MOVIE)

    music_genres = json.load(open('resources/data/genre/music.json'))
    for mg in music_genres:
        Genre.objects.create(name=mg, type=GenreType.MUSIC)


def generate_actors():
    actors = json.load(open('resources/data/actors.json'))
    for a in actors:
        Actor.objects.create(name=a)


def generate_cuisines():
    cuisines = json.load(open('resources/data/cuisine.json'))
    for c in cuisines:
        Cuisine.objects.create(name=c)


def generate_foods():
    foods = json.load(open('resources/data/food.json'))
    for f in foods:
        Food.objects.create(name=f['name'])


def generate_hobbies():
    hobbies = json.load(open('resources/data/hobbies.json'))
    for h in hobbies:
        Hobby.objects.create(name=h['hobby'])


def generate_movies():
    movies = json.load(open('resources/data/movies.json'))
    for m in movies:
        movie = Movie.objects.create(name=m['title'])
        for g in m['genres']:
            genre, created = Genre.objects.get_or_create(type=GenreType.MOVIE, name=g)
            movie.genre.add(genre)


def generate_songs():
    songs = json.load(open('resources/data/songs.json'))
    for s in songs:
        artist, created = Artist.objects.get_or_create(name=s['artist'])
        album, created = Album.objects.get_or_create(name=s['album'], artist=artist)
        Song.objects.create(name=s['title'], artist=artist, album=album)


def generate_sports():
    sports = json.load(open('resources/data/sports.json'))
    for s in sports:
        Sport.objects.create(name=s)


def generate_tv_shows():
    shows = json.load(open('resources/data/tv.json'))
    for s in shows:
        TvShow.objects.create(name=s)


def clean_up():
    Genre.objects.all().delete()
    Actor.objects.all().delete()
    Cuisine.objects.all().delete()
    Artist.objects.all().delete()
    Album.objects.all().delete()
    TvShow.objects.all().delete()
    Sport.objects.all().delete()
    Song.objects.all().delete()
    Movie.objects.all().delete()
    Hobby.objects.all().delete()
    Food.objects.all().delete()


class Command(BaseCommand):

    def handle(self, *args, **options):
        # clean_up()
        generate_genres()
        generate_actors()
        generate_cuisines()
        generate_foods()
        generate_hobbies()
        generate_movies()
        generate_songs()
        generate_sports()
        generate_tv_shows()
