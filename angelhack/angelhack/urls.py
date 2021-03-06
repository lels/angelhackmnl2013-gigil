from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from angel import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'angelhack.views.home', name='home'),
    # url(r'^angelhack/', include('angelhack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^angel/', include('angel.urls')),
)

if settings.DEBUG:
  urlpatterns += patterns('', \
       (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
       'django.views.static.serve', \
       {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}))

