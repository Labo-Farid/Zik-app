from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from video.forms import *
from .models import *


# Create your views here.

class clips_officiel_View(ListView):
    model = Clip
    paginate_by = 12
    template_name = 'video/clips_home.html'

    def get_context_data(self, **kwargs):

        clip_published = Clip.objects.all().filter(status='published').order_by('-timestamp')

        context = super().get_context_data(**kwargs)
        context['clip_published'] = clip_published

        context['page_request_var'] = "page"

        return context


def clip_category(request, cats):
    category_clips = Video.objects.filter(categories=cats)
    category_clips = category_clips.filter(status='published')

    paginator = Paginator(category_clips, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'category_clips': category_clips,
        'queryset': paginated_queryset,
        'cats': cats,
        'page_request_var': page_request_var,
    }
    return render(request, 'video/video_category.html', context)


class clip_officiel_DetailView(DetailView):
    model = Clip
    template_name = "video/clip_detail.html"

    def get_context_data(self, **kwargs):
        clip = get_object_or_404(Clip, slug=self.kwargs.get('slug'))

        clip_published = Clip.objects.all().filter(status='published').order_by('-timestamp')

        related_clip_officiel = Clip.objects.filter(category=clip.category).order_by('-created').exclude(id=clip.id)[:9]

        context = super().get_context_data(**kwargs)

        context['related_clip_officiel'] = related_clip_officiel
        context['clip_published'] = clip_published

        context['page_request_var'] = "page"
        return context


class CategoryClip(ListView):
    model = Clip
    template_name = "video/clip_category.html"
    
    def get_queryset(self):
        self.category = get_object_or_404(MusicCategory, slug=self.kwargs['slug'])
        return Clip.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryClip, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context