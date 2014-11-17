__author__ = 'Aiida'
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from InstrumentSeller.forms import *
from InstrumentSeller.models import *

class LoginFormMiddleware(object):
    def process_request(self, request):
        if request.method == 'POST' and 'login_form' in request.POST:
            loginform = login_form(request.POST)
            if loginform.is_valid():
                u = authenticate(username = loginform.cleaned_data['username'], password = loginform.cleaned_data['password'])
                if u is not None:
                    auth_login(request, u)
                    return HttpResponseRedirect('/')
                else:
                    error = 'Invalid Username/Password'
                # log the user in
                # if this is the logout page, then redirect to /
                # so we don't get logged out just after logging in
                if '/logout/' in request.get_full_path():
                    return HttpResponseRedirect('/')
        if request.method == 'POST' and 'reg_form' in request.POST:
            regform = register_form(request.POST)
            if regform.is_valid():
                if regform.cleaned_data['pass1'] != regform.cleaned_data['pass2']:
                    error = 'password mismatch'
                elif User.objects.filter(email = regform.cleaned_data['email']).count() > 0 :
                    error = 'Email exists'
                else:
                    user = User_Profile()
                    User.objects.create_user(username = regform.cleaned_data['email'], password=regform.cleaned_data['pass1'], email = regform.cleaned_data['email'], first_name=regform.cleaned_data['first_name'], last_name=regform.cleaned_data['family_name'])
                    u = authenticate(username = regform.cleaned_data['email'], password = regform.cleaned_data['pass1'])
                    if u is not None:
                        auth_login(request, u)
                    user.user = u
                    user.allowed_ad_count = 2
                    user.save()
                    return HttpResponseRedirect('/', locals())
        else:
            loginform = login_form()
            regform = register_form()
        # attach the form to the request so it can be accessed within the templates
        request.login_form = loginform
