from django import template

from music.models import *
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404

from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,

)

register = template.Library()


@register.inclusion_tag('music/snippets/recent_musics.html')
def render_recent_musics():
    musics = Music.objects.filter( status='published')
    recent_musics = musics.order_by('-created')[:6]
    return {
        'recent_musics': recent_musics
    }



@register.inclusion_tag('music/snippets/popular_musics.html')
def render_popular_musics():
    musics = Music.objects.filter( is_popular=True, status='published')
    popular_musics = musics.order_by('-created')[:10]
    return {
        'popular_musics': popular_musics
    }



@register.inclusion_tag('music/snippets/top_musics.html')
def render_top_musics():
    musics = Music.objects.filter(is_on_top=True, status='published')
    top_musics = musics.order_by('-created')[:1]
    return {
        'top_musics': top_musics
    }
    

# @register.inclusion_tag('music/snippets/category_musics.html')
# def render_musics_category(category=None, tag_slug=None):
#     musics = Music.objects.filter( status='published')
#     categories = MusicCategory.objects.all()

#     tag = None
#     if category:
#         category = get_object_or_404(MusicCategory, slug=category)
#         musics = musics.filter(category=category).order_by("-created")
    
#     if tag_slug:
#         tag = get_object_or_404(MusicTags, slug=tag_slug)
#         musics = musics.filter(tags__in=[tag])
    
        
#     return {
#         'musics': musics,
#         'categories': categories,
#         'category': category,
#         'tag': tag,
#     }
    

