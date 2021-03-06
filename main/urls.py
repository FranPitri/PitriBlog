from django.conf.urls import patterns, include, url
from django.views.generic.edit import UpdateView

urlpatterns = patterns('',
                       url(r'^$',
                           'main.views.home',
                           name='home'),
                       url(r'^publications/(?P<id_post>\d+)/$',
                           'main.views.article',
                           name='gotopost'),
                       url(r'^newarticle/$',
                           'main.views.newpost',
                           name='addpost'),
                      )
