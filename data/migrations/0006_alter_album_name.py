# Generated by Django 4.1.5 on 2023-01-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_remove_artist_genre_alter_song_genre_album_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
