from django.contrib import admin
from .models import *


# Register your models here.

class EventVideoAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'status', 'timestamp'
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'timestamp']
    ordering = ('status', 'timestamp')
    search_fields = ['title', 'description', 'event_category']


class EventImageAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'status', 'timestamp'
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category', 'timestamp']
    ordering = ('status', 'timestamp')
    search_fields = ['title', 'description', 'event_category']


class EventCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class EventTagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(EventVideo, EventVideoAdmin)
admin.site.register(EventImage, EventImageAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
admin.site.register(EventTags, EventTagsAdmin)
