from django.contrib import admin
from .models import *


# Register your models here.

class EmissionVideoAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'status', 'timestamp'
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'timestamp']
    ordering = ('status', 'timestamp')
    search_fields = ['title', 'description', 'event_category']


class EmissionPodcastAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'status', 'timestamp'
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'timestamp']
    ordering = ('status', 'timestamp')
    search_fields = ['title', 'description', 'event_category']


class EmissionCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class EmissionTagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    

class EmissionVideoCommentAdmin(admin.ModelAdmin):
    list_display = [ 'created']
    
    
class EmissionPodcastCommentAdmin(admin.ModelAdmin):
    list_display = [ 'created']


admin.site.register(EmissionPodcast, EmissionPodcastAdmin)
admin.site.register(EmissionVideo, EmissionVideoAdmin)
admin.site.register(EmissionCategory, EmissionCategoryAdmin)
admin.site.register(EmissionTags, EmissionTagsAdmin)
admin.site.register(EmissionVideoComment, EmissionVideoCommentAdmin)
admin.site.register(EmissionPodcastComment, EmissionPodcastCommentAdmin)
