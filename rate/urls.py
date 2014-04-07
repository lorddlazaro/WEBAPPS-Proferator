from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from rate.models import *

urlpatterns = patterns('',
    # ex: /polls/
    # url(r'^', views.index, name='index'),
    #url(r'^$', views.signup, name='signup'),
    url(r'^$', ListView.as_view(
        queryset = Professor.objects.all().order_by("-name")[:10],
    	template_name="index.html")),
    #url for the professor list order by ratings
    # ex: /polls/5/
    #url(r'^(?P<course_id>\d+)/searchresults/$', ListView.as_view(
    #    queryset = ProfessorView.objects.all().order_by("-name") [:5],
    #    template_name="searchresults.html")),

    # # ex: /polls/5/vote/
    # url(r'^(?P<professor_id>\d+)/rate/$', views.rate, name='rate'),
)