from django.urls import path, include
from .views import *
from .clips_views import *
from .teaser_views import *

urlpatterns = [
    path('', video_View.as_view(), name='videos'),
    path('videos/category/<slug>/', CategoryVideo.as_view(), name='category_video'),
    path('videos/<slug>/', video_DetailView.as_view(), name='video_detail'),
    
    path('clips/', clips_officiel_View.as_view(), name='clips'),
    path('clips/category/<slug>/', CategoryClip.as_view(), name='category_clip'),
    path('clips/<slug>/', clip_officiel_DetailView.as_view(), name='clip_detail'),
    
    path('teasers', teaser_View.as_view(), name='teasers'),
    path('teasers/category/<slug>/', CategoryTeaser.as_view(), name='category_teaser'),
    path('teasers/<slug>/', teaser_DetailView.as_view(), name='teaser_detail'),
]

