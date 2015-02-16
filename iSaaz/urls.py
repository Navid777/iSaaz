from InstrumentSeller import views
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from iSaaz import settings
from Content import views as Content_Views
from Directory import views as Directory_Views

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
    url(r'^home/search/$', views.home_search),
    url(r'^sell/$', views.sell),
    url(r'^get_shahrs/$', views.shahr),
    url(r'^get_mahales/$', views.mahale),
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
    url(r'^fav/(\d+)/(\d+)/$',views.fav),
    url(r'^delete_offer/(\d+)/$', views.delete_offer),
    url(r'^search/category/(\w+)/$', views.search_by_category),
    url(r'^delete_ad/(\d+)/$', views.delete_ad),
    url(r'^$', views.temp),
    url(r'^articles/$', Content_Views.articles),
    url(r'^articles/search/$', Content_Views.article_search),
    url(r'^articles/(\d+)/$', Content_Views.view_article),
    url(r'^search/articles/(\w+)/$', Content_Views.search_by_category),
    url(r'^like_article/$',Content_Views.like_article, name='likes'),
    url(r'^like_comment/$',Content_Views.comment_like),
  #  url(r'^reply/(\d+)/$',Content_Views.reply),
    url(r'^master/(\d+)/$',Directory_Views.master),
    url(r'^shop/(\d+)/$',Directory_Views.shop),
    url(r'^shops/$',Directory_Views.shops),
    url(r'^get_shops/$', Directory_Views.get_shops),
    url(r'^institute/(\d+)/$',Directory_Views.institute),
    url(r'^workshop/(\d+)/$',Directory_Views.workshop),
    url(r'^manufacturer/(\d+)/$',Directory_Views.manufacturer),
    url(r'^new_directory/$',Directory_Views.new_directory),
    url(r'^directories/$',Directory_Views.directories),
    url(r'^directories/master_search/$',Directory_Views.masters_search),
    url(r'^directories/saaz_search/$',Directory_Views.saaz_search),
    url(r'^directories/institutes_search/$',Directory_Views.institutes_search),
    url(r'^directories/?saaz=(\d+)$',Directory_Views.search),
)
#urlpatterns += patterns('django.views.generic.simple',&nbsp(r'^accounts/login/$', 'direct_to_template', {'template': 'login_required.html'}),)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
