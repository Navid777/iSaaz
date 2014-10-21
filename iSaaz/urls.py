from InstrumentSeller import views
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from iSaaz import settings
admin.autodiscover()

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
    
    
    url(r'^home$', views.home),
    url(r'^sell/$', views.sell),
    url(r'^profile/$', views.profile),
    url(r'^profile/listing$', views.profile_listing),
    url(r'^profile/messages$', views.profile_messages),
    url(r'^profile/show/message/(\d+)/$',views.profile_show_message),
    url(r'^profile/invoices$', views.profile_invoices),
    url(r'^profile/settings$', views.profile_settings),
    url(r'^compare$', views.compare),
    url(r'^instrument/(\d+)/$', views.instrument, name = "instrument"),
    url(r'^login/$', views.login_user),
    url(r'^logout/$', views.logout_user),
    url(r'^fav/(\d+)/(\d+)$',views.fav),
    url(r'^delete_offer/(\d+)/$', views.delete_offer),
    url(r'^$', views.temp),

)
#urlpatterns += patterns('django.views.generic.simple',&nbsp(r'^accounts/login/$', 'direct_to_template', {'template': 'login_required.html'}),)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
