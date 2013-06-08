from django.conf.urls import patterns, url
from django.conf.urls.static import static
from angel import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<student_id>\d+)/donate/$', views.donate, name='donate'),
)

