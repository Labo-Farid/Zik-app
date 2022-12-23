from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View

from blog.models import *
from event.models import *
from music.models import Music
from video.models import Video, Clip


# Create your views here.


def get_image_event_tag_count():
    queryset = EventImage \
        .objects \
        .values('tags__title') \
        .annotate(Count('tags__title'))
    return queryset


def get_video_event_tag_count():
    queryset = EventVideo \
        .objects \
        .values('tags__title') \
        .annotate(Count('tags__title'))
    return queryset


class EventHomeView(ListView):
    model = EventImage
    paginate_by = 12
    template_name = 'event/event_home.html'

    def get_context_data(self, **kwargs):
        tag_count = get_video_event_tag_count()

        video_event_published = EventVideo.objects.filter(status='published')
        image_event_published = EventImage.objects.filter(status='published')

        recent_video_events_published = video_event_published.order_by('-timestamp')[:6]
        recent_image_events_published = image_event_published.order_by('-timestamp')[:6]

        recent_video_events_sponsored = video_event_published.filter(is_sponsored=True).order_by('-timestamp')[:3]
        recent_image_events_sponsored = image_event_published.filter(is_sponsored=True).order_by('-timestamp')[:3]

        context = super().get_context_data(**kwargs)
        context['video_event_published'] = video_event_published
        context['image_event_published'] = image_event_published

        context['recent_video__events_published'] = recent_video_events_published
        context['recent_events_published'] = recent_image_events_published
        context['recent_video_events_sponsored'] = recent_video_events_sponsored
        context['recent_image_events_sponsored'] = recent_image_events_sponsored


        context['page_request_var'] = "page"
        context['tag_count'] = tag_count

        return context


class ImageEventDetailView(DetailView):
    model = EventImage
    template_name = "event/image_event_detail.html"

    def get_context_data(self, **kwargs):
        image_event = get_object_or_404(EventImage, slug=self.kwargs.get('slug'))

        context = super().get_context_data(**kwargs)

        context['page_request_var'] = "page"
        context['image_event'] = image_event
        return context


class VideoEventDetailView(DetailView):
    model = EventVideo
    template_name = "event/video_event_detail.html"

    def get_context_data(self, **kwargs):
        video_event = get_object_or_404(EventVideo, slug=self.kwargs.get('slug'))

        context = super().get_context_data(**kwargs)

        context['page_request_var'] = "page"
        context['video_event'] = video_event
        return context