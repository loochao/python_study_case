from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django .conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mydjangosite.views.home', name='home'),
                       # url(r'^mydjangosite/', include('mydjangosite.foo.urls')),
                       url(r'^$', 'blog.views.index', name='home'),
                       url(r'^blog/', include('blog.urls', namespace='blog')),
                       url(r'^polls/', include('polls.urls', namespace='polls')),
                       url(r'^signups/', include('signups.urls', namespace='signups')),
                       url(r'^rango/', include('rango.urls', namespace='rango')),
                       #url(r'^auth/', include('auth.urls', namespace='auth')),
                       #(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
