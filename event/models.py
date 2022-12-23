from ckeditor.fields import RichTextField
from django.db import models
from django_countries.fields import CountryField
from embed_video.fields import EmbedVideoField
from django.urls import reverse


# Create your models here.


class EventCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self) -> str:
        return self.title


class EventTags(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self) -> str:
        return self.title


class EventVideo(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = RichTextField()
    video = models.FileField(upload_to='Events/events_videos')
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='event_video_category')
    tags = models.ManyToManyField(EventTags)
    event_date = models.DateTimeField(null=True, blank=True)
    event_address = models.CharField(max_length=250, default='', null=True, blank=True)
    localisation = models.CharField(max_length=400, null=True, blank=True)
    contact_1 = models.IntegerField(max_length=30, null=True, blank=True)
    contact_2 = models.IntegerField(max_length=30, null=True, blank=True)
    country = CountryField(default='')
    is_sponsored = models.BooleanField(default=False)
    is_on_top = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, default='published', max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event:video_event_detail', kwargs={
            'slug': self.slug
        })


class EventImage(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='Events/events_images', max_length=200)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='event_image_category')
    tags = models.ManyToManyField(EventTags)
    event_date = models.DateTimeField(null=True, blank=True)
    event_address = models.CharField(max_length=250, default='', null=True, blank=True)
    localisation = models.CharField(max_length=400, null=True, blank=True)
    contact_1 = models.IntegerField(max_length=30, null=True, blank=True)
    contact_2 = models.IntegerField(max_length=30, null=True, blank=True)
    country = CountryField(default='')
    is_sponsored = models.BooleanField(default=False)
    is_on_top = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS_CHOICES, default='published', max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event:image_event_detail', kwargs={
            'slug': self.slug
        })
