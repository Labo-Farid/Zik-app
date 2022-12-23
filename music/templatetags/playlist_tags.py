from django import template

from music.models import Playlist

register = template.Library()


@register.inclusion_tag('playlist/snippets/recent_playlists.html')
def render_recent_playlists():
    playlists = Playlist.objects.filter( status='published')
    recent_playlists = playlists.order_by('-created')[:6]
    return {
        'recent_playlists': recent_playlists
    }

 
@register.inclusion_tag('playlist/snippets/popular_playlists.html')
def render_popular_playlists():
    playlists = Playlist.objects.filter( is_popular=True, status='published')
    popular_playlists = playlists.order_by('-created')[:6]
    print(popular_playlists)
    return {
        'popular_playlists': popular_playlists
    }



@register.inclusion_tag('playlist/snippets/top_playlists.html')
def render_top_playlists():
    playlists = Playlist.objects.filter( is_on_top=True, status='published')
    top_playlists = playlists.order_by('-created')[:1]
    return {
        'top_playlists': top_playlists
    }
