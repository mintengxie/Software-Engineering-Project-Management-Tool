from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from requirements.views import users
from requirements.views import home
from requirements import req_urls

urlpatterns = patterns(
    '',
    url(r'^$', home.home_page),
    # Project Management:
    url(r'^signin', users.signin),
    url(r'^signout', users.signout),
    url(r'^signup', users.signup), 
    url(r'^req/', include(req_urls)),
    # Communication:
    url(r'^communication/$', include('communication.urls')),
    # Issue Tracker:
    url(r'^issue_tracker/', include('issue_tracker.urls')),
    # Common Admin site:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    )
