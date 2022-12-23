from django.contrib import admin

from .models import *


class MusicCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class MusicTagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class MusicAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'is_on_top', 'status', 'created', 'artist'
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['artist', 'category', 'created']
    ordering = ('artist', 'status', 'created')
    search_fields = ['title', 'description', 'category']


class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



class PlaylistAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'is_on_top', 'status', 'created'
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['playlist_category', 'created']
    ordering = ('status', 'created')
    search_fields = ['title', 'description', 'playlist_category']


admin.site.register(MusicCategory, MusicCategoryAdmin)
admin.site.register(MusicTags, MusicTagsAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(PlaylistAudio)
admin.site.register(Playlist, PlaylistAdmin)
