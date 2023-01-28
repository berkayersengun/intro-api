from django.db import models

from accounts.models import User
from data.choices import GenreType


class SportType(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Sport(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # type = models.ForeignKey(SportType, models.CASCADE, null=False)


class Actor(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=30, choices=GenreType.choices)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name


class TvShow(models.Model):
    name = models.CharField(max_length=50, unique=True)
    genre = models.ForeignKey(Genre, models.CASCADE, null=True)


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, models.CASCADE, null=True)
    artist = models.ForeignKey(Artist, models.CASCADE, null=False)
    album = models.ForeignKey(Album, models.CASCADE, null=False)


class HobbyType(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Hobby(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(HobbyType, models.CASCADE, null=True)


class Cuisine(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # overriding str methods in model shows the actual value in the drf dropdown instead of showing object 1
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cuisine = models.ForeignKey(Cuisine, models.CASCADE, null=True)
    user = models.ManyToManyField(User)
