from django.urls import path, include
from .views import *
from marketing.views import *

app_name = 'event'

urlpatterns = [
    path('', EventHomeView.as_view(), name='event_home'),
    path('event-image/<slug>/', ImageEventDetailView.as_view(), name='image_event_detail'),
    path('event-video/<slug>/', VideoEventDetailView.as_view(), name='video_event_detail'),

]

