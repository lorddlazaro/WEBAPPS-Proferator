from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from rate.models import *
# Create your views here.

def index(request):
    latest_professor_list = Professor.objects.all()
    context = {'latest_professor_list':latest_professor_list}
    return render(request, 'rate/index.html', context)
    #template = loader.get_template('rate/index.html')
    #context = RequestContext(request, {
    #    'latest_professor_list': latest_professor_list,
    #})
    #return HttpResponse(template.render(context))

#class ResultsView(generic.ListView):
#    template_name = 'proferater/searchresult.html'
#    context_object_name = 'professor_list'
#    def get_queryset(self):
#        return Professor.objects.all()

def results(request, course_id):
    professor_list = Professor.objects.all()
    return render(request, 'proferater/searchresult.html', {'professor_list':professor_list})
    #return HttpResponse("You're Looking at the result of professor  search %s." % professor_id)

def profile(request, professor_id):
    #return HttpResponse("You're Looking at the professor profile %s " % professor_id)
    pass

def rate(request, professor_id):
    #return HttpResponse("You're Looking at the professor rate form %s" % professor_id)
    pass