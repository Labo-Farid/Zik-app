import random
import string

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from django.utils.translation import gettext as _

from video.models import *
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


def search(request):
    music_queryset = Music.objects.all()
    post_queryset = Post.objects.all()
    video_queryset = Video.objects.all()
    clip_queryset = Clip.objects.all()
    teaser_queryset = Teaser.objects.all()
    
    query = request.GET.get('q')
    if query:
        music_queryset = music_queryset.filter(
            Q(title__icontains=query)
        ).distinct()
    
    if query:
        post_queryset = post_queryset.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
        ).distinct()
        
    if query:
        video_queryset = video_queryset.filter(
            Q(title__icontains=query)
        ).distinct()
        
    if query:
        clip_queryset = clip_queryset.filter(
            Q(title__icontains=query)
        ).distinct()
        
    if query:
        teaser_queryset = teaser_queryset.filter(
            Q(title__icontains=query)
        ).distinct()

    paginator = Paginator(music_queryset, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'query': query,
        'music_queryset': music_queryset,
        'post_queryset': post_queryset,
        'video_queryset': video_queryset,
        'clip_queryset': clip_queryset,
        'teaser_queryset': teaser_queryset,

        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
    }
    return render(request, 'music/search_results.html', context)


def index(request):
    var = _("Bienvenue")

    return render(request, 'music/index.html', {'var': var})


class HomeView(ListView):
    model = Music
    paginate_by = 12
    template_name = 'music/musics.html'

    def get_context_data(self, **kwargs):

        musics_published = Music.objects.all().filter(status='published').order_by('-created')
        recent_musics = musics_published.order_by('-created')[:6]

        context = super().get_context_data(**kwargs)
        context['musics_published'] = musics_published
        context['recent_musics'] = recent_musics

        context['page_request_var'] = "page"

        return context


class MusicDetailView(DetailView):
    model = Music
    template_name = "music/music_detail.html"

    def get_context_data(self, **kwargs):
        music = get_object_or_404(Music, slug=self.kwargs.get('slug'))

        musics_published = Music.objects.all().filter(status='published').order_by('-created')

        related_musics = Music.objects.filter(category=music.category).order_by('-created').exclude(id=music.id)[:9]

        context = super().get_context_data(**kwargs)

        context['related_musics'] = related_musics
        context['musics_published'] = musics_published

        context['page_request_var'] = "page"
        return context


class CategoryMusic(ListView):
    model = Music
    template_name = "music/music_category.html"
    
    def get_queryset(self):
        self.category = get_object_or_404(MusicCategory, slug=self.kwargs['slug'])
        return Music.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryMusic, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


def DownloadSuccess(request, slug):
    music = Music.objects.get(slug=slug)
    music.download_count = music.download_count + 1
    music.save()
    
    context = {
        'music': music,
    }
    return render(request, 'music/download_success.html', context)