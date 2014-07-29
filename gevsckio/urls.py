from django.conf.urls import patterns, include, url
from django.conf import settings
from socketio import sdjango
sdjango.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^', include('echoesrv.urls')),
    url(r'^socket\.io', include(sdjango.urls)),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.urls.static import static

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
