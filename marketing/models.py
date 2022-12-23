from django.db import models
from django_countries.fields import CountryField

from music.models import MusicCategory


class Subscribers(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    country = CountryField(default='togo')
    phone = models.IntegerField()
    message = models.TextField(null=True)
    lu = models.BooleanField(default=False)
    fake = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# class AddMusicCategory(models.Model):
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200)
#
#     def __str__(self) -> str:
#         return self.name

class AddPremiumMusic(models.Model):
    artist_name = models.CharField(max_length=200)
    music_title = models.CharField(max_length=200)
    music_category = models.ForeignKey(MusicCategory, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='marketing/premium_musics/audios')
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='marketing/premium_musics/images')
    country = CountryField(default='togo')

    def __str__(self):
        return self.music_title + ' - ' + self.artist_name


class AddFreeMusic(models.Model):
    artist_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(MusicCategory, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='marketing/free_musics/audios')
    description = models.TextField()
    image = models.ImageField(upload_to='marketing/free_musics/images')
    country = CountryField(default='togo')

    def __str__(self):
        return self.title + ' - ' + self.artist_name
