from InstrumentSeller import views
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from iSaaz import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iSaaz.views.home', name='home'),
    # url(r'^iSaaz/', include('iSaaz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
    url(r'^$', views.home),
    url(r'^sell/$', views.sell),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)