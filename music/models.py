from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django.utils import timezone
from django_countries.fields import CountryField

User = get_user_model()


class MusicCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self) -> str:
        return self.name


class MusicTags(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    country = CountryField(default='togo')

    def __str__(self) -> str:
        return self.name


class Music(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.ForeignKey(MusicCategory, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='Musics/audios')
    description = models.TextField()
    image = models.ImageField(upload_to='Musics/images')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default='')
    tags = models.ManyToManyField(MusicTags)
    download_count = models.IntegerField(default=0, blank=True)
    is_on_top = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, default='published', max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("music:music_detail", kwargs={
            'slug': self.slug
        })
        
        

class PlaylistAudio(models.Model):
    title = models.CharField(max_length=200)
    audio = models.FileField(upload_to='Playlist/playlist_audios')
    image = models.ImageField(upload_to='Playlist/playlist_audios_images', default='playlist.PNG')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
        


class Playlist(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField()
    playlist_category = models.ForeignKey(MusicCategory, on_delete=models.CASCADE)
    music = models.ManyToManyField(PlaylistAudio)
    description = models.TextField()
    image = models.ImageField(upload_to='Playlist/images')
    tags = models.ManyToManyField(MusicTags)
    download_count = models.IntegerField(default=0, blank=True)
    is_on_top = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, default='published', max_length=20)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("music:playlist_detail", kwargs={
            'slug': self.slug
        })