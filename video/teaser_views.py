from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

from video.forms import *
from .models import *


# Create your views here.

class teaser_View(ListView):
    model = Teaser
    paginate_by = 12
    template_name = 'video/teaser_home.html'

    def get_context_data(self, **kwargs):

        teaser_published = Teaser.objects.all().filter(status='published').order_by('-timestamp')

        context = super().get_context_data(**kwargs)
        context['teaser_published'] = teaser_published

        context['page_request_var'] = "page"

        return context


class teaser_DetailView(DetailView):
    model = Teaser
    template_name = "video/teaser_detail.html"

    def get_context_data(self, **kwargs):
        video = get_object_or_404(Teaser, slug=self.kwargs.get('slug'))

        teaser_published = Teaser.objects.all().filter(status='published').order_by('-timestamp')

        related_teaser = Clip.objects.filter(category=video.category).order_by('-created').exclude(id=video.id)[:9]

        context = super().get_context_data(**kwargs)

        context['related_teaser'] = related_teaser
        context['teaser_published'] = teaser_published

        context['page_request_var'] = "page"
        return context


class CategoryTeaser(ListView):
    model = Teaser
    template_name = "video/teaser_category.html"
    
    def get_queryset(self):
        self.category = get_object_or_404(MusicCategory, slug=self.kwargs['slug'])
        return Teaser.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryTeaser, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context