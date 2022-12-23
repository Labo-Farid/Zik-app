from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *


class ClipAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


# admin.site.register(Clip, ClipAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'status', 'timestamp'
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'timestamp']
    ordering = ('status', 'timestamp')
    search_fields = ['title', 'description', 'category']
    
    
class TeaserAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'status', 'timestamp'
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'timestamp']
    ordering = ('status', 'timestamp')
    search_fields = ['title', 'description', 'category']


class ClipAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'status', 'timestamp'
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'timestamp']
    ordering = ('status', 'timestamp')
    search_fields = ['title', 'description', 'category']



admin.site.register(VideoComment)
admin.site.register(Clip, ClipAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Teaser, TeaserAdmin)
