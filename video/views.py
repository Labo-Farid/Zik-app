from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from video.forms import *
from .models import *


# Create your views here.

class video_View(ListView):
    model = Video
    paginate_by = 12
    template_name = 'video/video_home.html'

    def get_context_data(self, **kwargs):

        video_published = Video.objects.all().filter(status='published').order_by('-timestamp')

        context = super().get_context_data(**kwargs)
        context['video_published'] = video_published

        context['page_request_var'] = "page"

        return context


class video_DetailView(DetailView):
    model = Video
    template_name = "video/video_detail.html"

    def get_context_data(self, **kwargs):
        clip = get_object_or_404(Video, slug=self.kwargs.get('slug'))

        video_published = Video.objects.all().filter(status='published').order_by('-timestamp')

        related_clip_officiel = Clip.objects.filter(category=clip.category).order_by('-created').exclude(id=clip.id)[:9]

        context = super().get_context_data(**kwargs)

        context['related_clip_officiel'] = related_clip_officiel
        context['video_published'] = video_published

        context['page_request_var'] = "page"
        return context


class CategoryVideo(ListView):
    model = Video
    template_name = "video/video_category.html"
    
    def get_queryset(self):
        self.category = get_object_or_404(MusicCategory, slug=self.kwargs['slug'])
        return Video.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryVideo, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context