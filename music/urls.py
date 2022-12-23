from django.urls import path
from .views import *
from music.playlist_views import *
from music.playlist_views import *

app_name = 'music'

urlpatterns = [
    path('', index, name='home'),

    path('search/', search, name='search'),

    path('musics/', HomeView.as_view(), name='musics'),
    path('musics/category/<slug>/', CategoryMusic.as_view(), name='category_music'),
    path('music/<slug>/', MusicDetailView.as_view(), name='music_detail'),
    
    path('music/<slug>/download-success', DownloadSuccess, name='download_success'),

    path('playlists', PlaylistsView.as_view(), name='playlists'),
    path('playlists/category/<slug>/', CategoryPlaylist.as_view(), name='category_playlist'),
    path('playlist/<slug>/', PlaylistDetailView.as_view(), name='playlist_detail'),

]
