# -*- coding: utf-8 -*-
from InstrumentSeller.forms import *
from InstrumentSeller.models import *
from django.contrib import auth
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import json
from django.forms.models import model_to_dict
import django_trace

@csrf_protect
def home(request):
    mainAds = Advertisement.objects.all()
    ad = Advertisement.objects.all()
    categories = Category.objects.all()
    cat2 = categories.values_list('cat2',flat=True).distinct()
    if request.method == 'POST':
        search_form = home_search_form(request.POST)
        if search_form.is_valid():
            ostan = search_form.cleaned_data['home_ostan']
            shahr = search_form.cleaned_data['home_shahr']
            mahale = search_form.cleaned_data['home_mahale']
            saaz = search_form.cleaned_data['saaz']
            min = search_form.cleaned_data['min_price']
            max = search_form.cleaned_data['max_price']
            if ostan:
                print ("here")
                mainAds = Advertisement.objects.filter(location__ostan = ostan)
                if shahr:
                    mainAds = Advertisement.objects.filter(location__shahr = shahr)
                    if mahale:
                        mainAds = Advertisement.objects.filter(location__mahale = mahale)
            if saaz:
                mainAds = mainAds.filter(instrument__category__cat4 = saaz)
            if min:
                min = int(min)
                mainAds = mainAds.filter(price__lt = min)
            if max:
                max = int(max)
                mainAds = mainAds.filter(price__gt = max)
    search_form = home_search_form()
    return render(request, 'home.html', locals())

@csrf_protect
def home_search(request):
    mainAds = []
    ads = []
    if request.method == 'POST':
            ostan = request.POST.get('ostan')
            shahr = request.POST.get('shahr')
            mahale = request.POST.get('mahale')
            saaz = request.POST.get('saaz')
            min = request.POST.get('min_price')
            max = request.POST.get('max_price')
            print (ostan )
            if ostan:
                ads = Advertisement.objects.filter(location__ostan = ostan)
                if shahr:
                    ads = Advertisement.objects.filter(location__shahr = shahr)
                    if mahale:
                        ads = Advertisement.objects.filter(location__mahale = mahale)
            if saaz:
                ads = ads.filter(instrument__category__cat4 = saaz)
            if min:
                min = int(min)
                ads = ads.filter(price__lt = min)
            if max:
                max = int(max)
                ads = ads.filter(price__gt = max)
            for ad in ads:
                info = {}
                info['id'] = ad.id
                info['image'] = ad.image.image.url
                info['title'] = ad.title
                info['instrument'] = ad.instrument.name
                info['price'] = ad.price
                mainAds.append(info)
    return HttpResponse(json.dumps(mainAds), mimetype='application/javascript')

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
    return HttpResponseRedirect('/home')


@csrf_protect
def sell(request):
    if request.method == 'POST':    
        form = ad_form(request.POST, request.FILES)
        if form.is_valid():
            ad = Advertisement()
            saazid = build_ad(request, form, ad)
            if "auth_sub" in request.POST:
                user = User_Profile()
                user.user = request.user
                user.allowed_ad_count = 2
                user.save()
                ad.user = user
                ad.save()
                return HttpResponseRedirect('/instrument/%d/' % saazid)
            elif "login_sub" in request.POST:
                lform = login_form(request.POST)
                if lform.is_valid():
                    u = authenticate(username = lform.cleaned_data['username'], password = lform.cleaned_data['password'])
                    if u is not None:
                        auth_login(request, u)
                        user = u.profile
                        ad.user = user
                        ad.save()
                        return HttpResponseRedirect('/instrument/%d/' % saazid)
                    else:
                        error = 'Invalid Username/Password'
            elif "reg_sub" in request.POST:
                rform = register_form(request.POST)
                if rform.is_valid():
                    if rform.cleaned_data['pass1'] != rform.cleaned_data['pass2']:
                        error = 'password mismatch'
                    elif User.objects.filter(email = rform.cleaned_data['email']).count() > 0 :
                        error = 'Email exists'
                    else:
                        user = User_Profile()
                        User.objects.create_user(username = rform.cleaned_data['email'], password=rform.cleaned_data['pass1'], email = rform.cleaned_data['email'], first_name=rform.cleaned_data['first_name'], last_name=rform.cleaned_data['family_name'])
                        u = authenticate(username = rform.cleaned_data['email'], password = rform.cleaned_data['pass1'])
                        if u is not None:
                            auth_login(request, u)
                        user.user = u
                        user.allowed_ad_count = 2
                        user.save()
                        ad.user = user
                        ad.save()
                        return HttpResponseRedirect('/profile/settings', locals())
    else:
        form = ad_form()
        lform = login_form()
        rform = register_form()
    return render_to_response('sell.html', RequestContext(request,locals()))

def build_ad(request, form, ad):
    saaz = Instrument()
    saaz.name = form.cleaned_data['sell_sub4']
    saaz.manufacturer = form.cleaned_data['manufacturer']
    saaz.model = form.cleaned_data['model']
    saaz.year = form.cleaned_data['year']
    saaz.used = form.cleaned_data['used']
    saaz.save()
    category = Category()
    category.cat1 = form.cleaned_data['sell_sub1']
    category.cat2 = form.cleaned_data['sell_sub2']
    category.cat3 = form.cleaned_data['sell_sub3']
    category.cat4 = form.cleaned_data['sell_sub4']
    category.save()
    saaz.category = category
    img1 = Ad_Image(image = request.FILES['img1'])
    img1.save()
    ad.image = img1
    ad.instrument = saaz
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
    location.ostan = form.cleaned_data['sell_ostan']
    location.shahr= form.cleaned_data['sell_shahr']
    location.mahale = form.cleaned_data['sell_mahale']
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
    ad.show_email = form.cleaned_data['show_email']
    ad.show_tel = form.cleaned_data['show_tel']
    ad.save()
    saaz.ad.add(ad)
    saaz.save()
    return ad.id

def profile(request):
    user = User_Profile.objects.get(user = request.user.id)
    ads = user.Ads.all()
    unread = []
    for a in ads:
        for o in a.offers.all():
            if o.read == False:
                unread.append(o)
    return render(request, 'profile.html', locals())

def profile_listing(request):
    user = User_Profile.objects.get(user = request.user)
    ads = user.Ads.all
    return render(request, 'profile_listing.html', locals())

def profile_messages(request):
    user = User_Profile.objects.get(user = request.user)
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
    user = User_Profile.objects.get(user = request.user)
    return render(request, 'profile_invoices.html')

@csrf_protect
def profile_settings(request):
    user = User_Profile.objects.get(user = request.user)
    if request.POST:
        if 'form1' in request.POST:
            form1 = profile_form1(request.POST, prefix= 'form1')
            if form1.is_valid():
                user.user.email = form1.data['email']
                user.user.username = form1.data['email']
                pass1 = form1.cleaned_data.get('password1', None)
                pass2 = form1.cleaned_data.get('password2', None)
                if pass1 and pass2 and (pass1 == pass2):
                    user.user.set_password(form1.cleaned_data['password1'])

        elif 'form2' in request.POST:
            form2 = profile_form2(request.POST, prefix= 'form2')
            if form2.is_valid():
                user.user.first_name = form2.data['name']
                user.user.last_name = form2.data['family_name']
                user.tel = form2.data['tel']
        elif 'form3' in request.POST:
            form3 = profile_form3(request.POST, prefix= 'form3')
        user.user.save()
        user.save()

    form3 = profile_form3(prefix= 'form3')
    form1 = profile_form1(prefix= 'form1')
    form2 = profile_form2(prefix= 'form2')
    return render(request, 'profile_settings.html', locals())

def compare(request):
    ads = Advertisement.objects.all()
    return render(request, 'compare.html', locals())

@csrf_protect
def instrument(request, ad_id):
    ad = Advertisement.objects.get(id = ad_id)
    instrument = ad.instrument
    if request.POST:
        form = offer_form(request.POST)
        if form.is_valid():
            offer = Offer()
            offer.sender= form.cleaned_data['sender']
            offer.email= form.cleaned_data['email']
            offer.price = form.cleaned_data['price']
            offer.tel = form.cleaned_data['tel']
            offer.transport = form.cleaned_data['transport']
            offer.content = form.cleaned_data['content']
            offer.ad = ad
            offer.save()
        else:
            error = "نم"
    form = offer_form()
    return render(request, 'instrument.html', locals())

def delete_ad(request, ad_id):
    Advertisement.objects.get(id = ad_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete_offer(request, offer_id):
    Offer.objects.get(id = offer_id).delete()
    return HttpResponseRedirect('/profile/messages')

def fav(request, user_id, ad_id):
    user = User_Profile.objects.get(id = user_id)
    ad = Advertisement.objects.get(id = ad_id)
    user.favorite.add(ad)
    user.save()
    ad.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def temp(request):
    return render(request, 'temp.html')

def search_by_category(request, category_name):
    categories = Category.objects.all()
    cat2 = categories.values_list('cat2',flat=True).distinct()
    mainAds = Advertisement.objects.filter(instrument__category__cat2=category_name)
    ads = Advertisement.objects.all()
    return render(request, 'home.html', locals())
    
