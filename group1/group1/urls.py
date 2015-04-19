from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$',
                           'project_router.views.home_page',
                           name='home'
                           ),
                       url(r'^requirements/$',
                           include('requirements.urls')
                           ),
                       url(r'^communication/$',
                           include('communication.urls')
                           ),
                       url(r'^issue_tracker/',
                           include('issue_tracker.urls')
                           ),
                       # url(r'^admin/', include(admin.site.urls)),
                       )