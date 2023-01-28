from django.db import models


class GenreType(models.TextChoices):
    MOVIE = 'Movie'
    # TV_SHOW = 'Tv Show'
    MUSIC = 'Music'
