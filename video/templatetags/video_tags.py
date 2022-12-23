from django import template

from video.models import Teaser
from video.models import Video
from video.models import Clip

register = template.Library()


@register.inclusion_tag('video/snippets/recent_videos.html')
def render_recent_videos():
    videos = Video.objects.filter( status='published')
    recent_videos = videos.order_by('-timestamp')[:6]
    return {
        'recent_videos': recent_videos
    }


@register.inclusion_tag('video/snippets/recent_teasers.html')
def render_recent_teasers():
    teasers = Teaser.objects.filter(  status='published')
    recent_teasers = teasers.order_by('-timestamp')[:6]
    return {
        'recent_teasers': recent_teasers
    }


@register.inclusion_tag('video/snippets/recent_clips.html')
def render_recent_clips():
    clips = Clip.objects.filter(status='published')
    recent_clips = clips.order_by('-timestamp')[:6]
    return {
        'recent_clips': recent_clips
    }


@register.inclusion_tag('video/snippets/popular_clips.html')
def render_popular_clips():
    clips = Clip.objects.filter(status='published', is_popular=True)
    popular_clips = clips.order_by('-timestamp')[:6]
    return {
        'popular_clips': popular_clips
    }


@register.inclusion_tag('video/snippets/popular_teasers.html')
def render_popular_teasers():
    teasers = Teaser.objects.filter(status='published',   is_popular=True)
    popular_teasers = teasers.order_by('-timestamp')[:6]
    return {
        'popular_teasers': popular_teasers
    }


@register.inclusion_tag('video/snippets/popular_videos.html')
def render_popular_videos():
    videos = Video.objects.filter(status='published',  is_popular=True)
    popular_videos = videos.order_by('-timestamp')[:6]
    return {
        'popular_videos': popular_videos
    }


@register.inclusion_tag('video/snippets/top_teasers.html')
def render_top_teasers():
    teasers = Teaser.objects.filter(status='published',   is_on_top=True)
    top_teasers = teasers.order_by('-timestamp')[:1]
    return {
        'top_teasers': top_teasers
    }


@register.inclusion_tag('video/snippets/top_videos.html')
def render_top_videos():
    videos = Video.objects.filter(status='published',  is_on_top=True)
    top_videos = videos.order_by('-timestamp')[:1]
    return {
        'top_videos': top_videos
    }


@register.inclusion_tag('video/snippets/top_clips.html')
def render_top_clips():
    clips = Clip.objects.filter(status='published', is_on_top=True)
    top_clips = clips.order_by('-timestamp')[:1]
    return {
        'top_clips': top_clips
    }
