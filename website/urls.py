from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('video/', include('video.urls')),
    path('marketing/', include('marketing.urls', namespace='marketing')),
    path('event/', include('event.urls', namespace='event')),
    path('emission/', include('emission.urls', namespace='emission')),
    path('tinymce/', include('tinymce.urls')),

    url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('api/blog/', include('blog.api.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('music.urls', namespace='music')),
    path('accounts/', include('allauth.urls')),
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

if not settings.DEBUG:
    urlpatterns += [re_path(r'^.*',
                            TemplateView.as_view(template_name='index.html'))]
