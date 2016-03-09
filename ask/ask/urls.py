from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'[\w\d]*', include('qa.urls')),
    url(r'^login/', include('qa.urls')),
    url(r'^signup/', include('qa.urls')),
    url(r'^question/[0-9]+/', include('qa.urls')),
    url(r'^ask/', include('qa.urls')),
    url(r'^popular/', include('qa.urls')),
    url(r'^new/', include('qa.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
