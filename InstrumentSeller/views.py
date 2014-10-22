# -*- coding: utf-8 -*-
from InstrumentSeller.forms import *
from InstrumentSeller.models import *
from django.contrib import auth
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

def home(request):
    mainAds = Advertisement.objects.all()
    ad = Advertisement.objects.all()
    return render(request,'home.html', locals())

@csrf_protect
def login_user(request):
    if request.method == 'POST':
        f = login_form(request.POST)
        if f.is_valid():
            u = authenticate(username = f.cleaned_data['username'], password = f.cleaned_data['password'])
            if u is not None:
                auth_login(request, u)
                return HttpResponseRedirect('/')
            else:
                error = 'Invalid Username/Password'
    f = login_form()
    return render_to_response('login.html', RequestContext(request,locals()))

def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@csrf_protect
def sell(request):
    if request.method == 'POST':    
        form = ad_form(request.POST, request.FILES)
        if form.is_valid():
            saaz = Instrument()
            ad = Advertisement()
            saaz.name = form.cleaned_data['sub4']
            saaz.manufacturer = form.cleaned_data['manufacturer']
            saaz.model = form.cleaned_data['model']
            saaz.year = form.cleaned_data['year']
            if form.cleaned_data['used'] == 'دست دو':
                saaz.used = True
            saaz.save()
            category = Category()
            category.cat1 = form.cleaned_data['sub1']
            category.cat2 = form.cleaned_data['sub2']
            category.cat3 = form.cleaned_data['sub3']
            category.cat4 = form.cleaned_data['sub4']
            category.save()
            saaz.category = category
            user = User_Profile()
            user.user = User.objects.get(id = 1)
            user.allowed_ad_count = 2
            user.save()
            img1 = Ad_Image(image = request.FILES['img1'])
            img1.save()
            ad.image = img1
            ad.instrument = saaz
            ad.user = user
            ad.used = form.cleaned_data['used']
            ad.title = form.cleaned_data['title']
            ad.details = form.cleaned_data['details']
            ad.transport = form.cleaned_data['transport']
            ad.returning = form.cleaned_data['returning']
            ad.purchase = form.cleaned_data['purchase']
            ad.price = int(form.cleaned_data['price'])
            if 'sound' in request.FILES:
                ad.sound = request.FILES['sound']
            location = Location()
            location.ostan = form.cleaned_data['ostan']
            location.shahr= form.cleaned_data['shahr']
            location.mahale = form.cleaned_data['mahale']
            location.save()
            ad.location = location
            ad.save()
            ad.images.add(img1)
            if 'img2' in request.FILES:
                img2 = Ad_Image(image = request.FILES['img2'])
                img2.save()
                ad.images.add(img2)
            if 'img3' in request.FILES:
                img3 = Ad_Image(image = request.FILES['img3'])
                img3.save()
                ad.images.add(img3)
            if 'img4' in request.FILES:
                img4 = Ad_Image(image = request.FILES['img4'])
                img4.save()
                ad.images.add(img4)
            if 'img5' in request.FILES:
                img5 = Ad_Image(image = request.FILES['img5'])
                img5.save()
                ad.images.add(img5)
            if 'img6' in request.FILES:
                img6 = Ad_Image(image = request.FILES['img6'])
                img6.save()
                ad.images.add(img6)
            ad.save()
            saaz.ad.add(ad)
            saaz.save()
            return HttpResponseRedirect('/instrument/%d/' % saaz.id)
    else:
        form = ad_form()
    return render_to_response('sell.html', RequestContext(request,locals()))

def profile(request):
    user = User_Profile.objects.get(id = 2)
    ads = user.Ads.all()
    unread = []
    for a in ads:
        for o in a.offers.all():
            if o.read == False:
                unread.append(o)
    return render(request, 'profile.html', locals())

def profile_listing(request):
    user = User_Profile.objects.get(id = 1)
    ads = user.Ads.all
    return render(request, 'profile_listing.html', locals())

def profile_messages(request):
    user = User_Profile.objects.get(id = 2)
    offers = []
    ads = user.Ads
    for i in ads.all():
        for o in i.offers.all():
            offers.append(o)
    return render(request, 'profile_messages.html', locals())

def profile_show_message(request, o_id):
    offer = Offer.objects.get(id = o_id)
    offer.read = True
    offer.save()
    return render(request, 'profile_show_message.html', locals())

def profile_invoices(request):
    return render(request, 'profile_invoices.html')

@csrf_protect
def profile_settings(request):
    user = User_Profile.objects.get(id = 2)
    if request.POST:
        if 'form1' in request.POST:
            form1 = profile_form1(request.POST, prefix= 'form1')
            if form1.is_valid():
                user.user.email = form1.data['email']
                pass1 = form1.cleaned_data.get('password1', None)
                pass2 = form1.cleaned_data.get('password2', None)
                if pass1 and pass2 and (pass1 == pass2):
                    user.user.set_password(form1.cleaned_data['password1'])

        elif 'form2' in request.POST:
            form2 = profile_form2(request.POST, prefix= 'form2')
            if form2.is_valid():
                user.user.first_name = form2.cleaned_data['name']
                user.user.last_name = form2.cleaned_data['family_name']
                user.tel = int(form2.cleaned_data['tel'])
        elif 'form3' in request.POST:
            form3 = profile_form3(request.POST, prefix= 'form3')
        user.user.save()
        user.save()

    form3 = profile_form3(prefix= 'form3')
    form1 = profile_form1(prefix= 'form1')
    form2 = profile_form2(prefix= 'form2')
    return render(request, 'profile_settings.html', locals())

def compare(request):
    return render(request, 'compare.html')

def instrument(request, instrument_id):
    instrument = Instrument.objects.get(id = instrument_id)
    ad = instrument.ad.all
    return render(request, 'instrument.html', locals())

def temp(request):
    return render(request, 'temp.html')