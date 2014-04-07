from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/proferater/search/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
    return render_to_response('index.html')

def invalid_login(request):
    return render_to_response('login.html')
    #invalid not yet working

def logout(request):
    auth.logout(request)
    return render_to_response('home.html')

def register_user(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()
    #print args
    return render_to_response('signup.html', args)

def register_success(request):
    return render_to_response('/proferater/home/')

def professor_profile(request):
    return render_to_response('professor-profile.html')

def view_rate(request):
    return HttpResponseRedirect('/proferater/rate/')

def rate(request):
    return render_to_response('rate-comment-form.html')

def search(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
        return render_to_response('index.html')
