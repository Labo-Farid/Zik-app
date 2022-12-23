from ckeditor.fields import RichTextField
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from django.urls import reverse


# Create your models here.


class EmissionCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self) -> str:
        return self.title


class EmissionTags(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self) -> str:
        return self.title


class EmissionPodcast(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    audio = models.FileField(upload_to='Emission/emission_podcasts')
    episode = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='Emission/emission_podcasts_images', default='emission.JPG')
    description = models.TextField()
    category = models.ForeignKey(EmissionCategory, on_delete=models.CASCADE, related_name='emission_podcast_category')
    tags = models.ManyToManyField(EmissionTags)
    date = models.DateTimeField(null=True, blank=True)
    country = CountryField(default='')
    is_on_top = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, default='published', max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('emission:emission_podcast_detail', kwargs={
            'slug': self.slug
        })
        
    def get_comments(self):
        return self.emission_podcast_comments.all()
        
        
class EmissionPodcastComment(models.Model):
    emission_podcast = models.ForeignKey(
        EmissionPodcast, on_delete=models.CASCADE, related_name='emission_podcast_comments')
    # username = models.CharField(max_length=100)
    # email = models.EmailField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emission_podcast.title
    
    def get_absolute_url(self):
        return reverse('emission:emission_podcast_detail', kwargs={
            'slug': self.slug
        })


class EmissionVideo(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    video = models.FileField(upload_to='Emission/emission_videos')
    episode = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='Emission/emission_videos_images', default='emission.jpg')
    description = models.TextField()
    category = models.ForeignKey(EmissionCategory, on_delete=models.CASCADE, related_name='emission_video_category')
    tags = models.ManyToManyField(EmissionTags)
    emission_date = models.DateTimeField(null=True, blank=True)
    country = CountryField(default='')
    is_on_top = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, default='published', max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('emission:emission_video_detail', kwargs={
            'slug': self.slug
        })
        
    def get_comments(self):
        return self.emission_video_comments.all()
        
        
class EmissionVideoComment(models.Model):
    emission_video = models.ForeignKey(
        EmissionVideo, on_delete=models.CASCADE, related_name='emission_video_comments')
    # username = models.CharField(max_length=100)
    # email = models.EmailField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emission_video.title
    
    def get_absolute_url(self):
        return reverse('emission:emission_video_detail', kwargs={
            'slug': self.slug
        })