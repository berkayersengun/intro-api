# Generated by Django 4.1.5 on 2023-01-10 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_genre_alter_artist_genre_alter_movie_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sport',
            name='type',
        ),
        migrations.AlterField(
            model_name='genre',
            name='type',
            field=models.CharField(choices=[('Movie', 'Movie'), ('Music', 'Music')], max_length=30),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='data.genre'),
        ),
    ]
