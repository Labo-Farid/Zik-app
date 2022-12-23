from django.urls import path, include

from marketing.views import *

app_name = 'marketing'

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('subscribe/', subscribe, name='subscribe'),
    path('mail_letter/', mail_letter, name='mail-letter'),
    path('user-add-free-music/', user_add_free_music, name='user_add_free_music'),
    path('user-add-premium-music/', user_add_premium_music, name='user_add_premium_music'),
]

