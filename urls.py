from django.conf.urls import patterns, url

from rate import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<course_id>\d+)/searchresults/$', views.results, name='results'),
    # ex: /polls/5/results/
    url(r'^(?P<professor_id>\d+)/profile/$', views.profile, name='profile'),
    # ex: /polls/5/vote/
    url(r'^(?P<professor_id>\d+)/rate/$', views.rate, name='rate'),
)