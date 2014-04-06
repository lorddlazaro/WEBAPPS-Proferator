from django.shortcuts import render, render_to_response, RequestContext
from django.views import generic
from django.utils import timezone

from rate.models import *
from .forms import SignUpForm
# Create your views here.

def index(request):
    latest_professor_list = Professor.objects.all().order_by
    context = {'latest_professor_list':latest_professor_list}
    return render(request, 'proferater/index.html', context)
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
    factor = get_object_or_404(FactorRating, v=value)
    r = Rating(time=timezone.now())
    selectedvalue = factor.value_set.get(value=request.POST['choice'])
    #f = Factor(name=, description=)
    return HttpResponse("You're Looking at the professor rate form %s" % professor_id)

def signup(request):
    form = SignUpForm
    return render_to_response("signup.html", locals(), context_instance=RequestContext(request))
