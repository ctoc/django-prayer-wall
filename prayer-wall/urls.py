from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UWMCCFsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^$', 'prayer-wall.views.home' ),
    url('/newrequest', 'prayer-wall.views.home' ),
    # url('/request/', 'prayer-wall.views.home' ),

)
