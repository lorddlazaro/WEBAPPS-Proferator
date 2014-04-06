from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proferater.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/docs', include('django.contrib.admindocs.urls')),
    url(r'^accounts/login/$', 'proferater.views.login'),
    url(r'^accounts/auth/$', 'proferater.views.auth_view'),
    url(r'^accounts/logout/$', 'proferater.views.logout'),
    url(r'^accounts/loggedin/$', 'proferater.views.loggedin'),
    url(r'^accounts/invalid/$', 'proferater.views.invalid_login'),
    url(r'^accounts/register/$', 'proferater.views.register_user'),
    url(r'^accounts/register_success/$', 'proferater.views.register_success'),
    #url(r'^proferater/',include('rate.urls',namespace="rate")),

)
