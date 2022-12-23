# from tinymce.models import HTMLField
from django.db import models
# from tinymce import models as tinymce_models
from  embed_video.fields  import  EmbedVideoField

from django.contrib.auth import get_user_model
from django.urls import reverse
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField

from music.models import Artist, MusicCategory

User = get_user_model()


class VideoComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_user')
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    video = models.ForeignKey(
        'Video', related_name='video_comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Video(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = RichTextField()
    video = models.FileField(upload_to='Videos/videos')
    thumbnail = models.ImageField(upload_to='Videos/videos_thumbnails', max_length=500, null=True, blank=True)
    category = models.ForeignKey(MusicCategory, on_delete=models.CASCADE, related_name='video_category')
    status = models.CharField(choices=STATUS_CHOICES, default='published', max_length=20)
    is_on_top = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={
            'slug': self.slug
        })
        
        
class Teaser(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = RichTextField()
    video = models.FileField(upload_to='Teaser/videos')
    thumbnail = models.ImageField(upload_to='Videos/videos_thumbnails', max_length=500, null=True, blank=True)
    category = models.ForeignKey(MusicCategory, on_delete=models.CASCADE, related_name='teaser_category')
    status = models.CharField(choices=STATUS_CHOICES, default='published', max_length=20)
    is_on_top = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('teaser_detail', kwargs={
            'slug': self.slug
        })



class Clip(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = RichTextField()
    clip = EmbedVideoField()
    thumbnail = models.ImageField(upload_to='Clip/clip_thumbnail', max_length=500, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default='')
    category = models.ForeignKey(MusicCategory, on_delete=models.CASCADE, related_name='clip_category')
    is_on_top = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, default='published', max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('clip_detail', kwargs={
            'slug': self.slug
        })
