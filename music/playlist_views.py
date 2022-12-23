import random
import string

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View

from video.models import Clip, Video
from .forms import *
from .models import *

from blog.views import *
from blog.forms import *
from blog.models import *

from django.shortcuts import render, redirect
from marketing.forms import SubscibersForm, MailMessageForm
from marketing.models import Subscribers
from django.core.mail import send_mail
from django_pandas.io import read_frame


class PlaylistsView(ListView):
    model = Playlist
    paginate_by = 12
    template_name = 'playlist/playlists_home.html'

    def get_context_data(self, **kwargs):
        playlists_published = Playlist.objects.all().filter(status='published').order_by('-created')
        
        context = super().get_context_data(**kwargs)
        context['playlists_published'] = playlists_published
        context['page_request_var'] = "page"
        return context



def get_audio_count():
    queryset = Playlist \
        .objects \
        .values('music__audio') \
        .annotate(Count('music__audio'))
    return queryset


class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = "playlist/playlist_detail.html"

    def get_context_data(self, **kwargs):
        
        playlist = get_object_or_404(Playlist, slug=self.kwargs.get('slug'))
        audio_count = get_audio_count()
        playlists_published = Playlist.objects.all().filter(status='published').order_by('-created')
        related_playlists = Music.objects.filter(category=playlist.playlist_category).order_by('-created').exclude(id=playlist.id)[:9]

        context = super().get_context_data(**kwargs)
        context['audio_count'] = audio_count
        context['related_playlists'] = related_playlists
        context['playlists_published'] = playlists_published
        context['playlist'] = playlist

        context['page_request_var'] = "page"
        return context


class CategoryPlaylist(ListView):
    model = Playlist
    template_name = "playlist/playlist_category.html"
    
    def get_queryset(self):
        self.category = get_object_or_404(MusicCategory, slug=self.kwargs['slug'])
        return Playlist.objects.filter(playlist_category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryPlaylist, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context