# -*- coding: utf-8 -*-
from Directory.models import *
from InstrumentSeller.models import *
from Content.models import  *
from InstrumentSeller.models import *
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import auth
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from Content.forms import *
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Directory.forms import *
import json
from django.views.decorators.csrf import csrf_protect


def has_saaz_autocomplete():
    category = []
    for c in Category.objects.all():
        category.append(c.cat3)
    return category

def master(request, master_id):
    master = Master.objects.get(id = master_id)
    return render_to_response('master.html', RequestContext(request,locals()))

def shop(request, shop_id):
    shop = Shop.objects.get(id = shop_id)
    return render_to_response('shop.html', RequestContext(request,locals()))

def shops(request):
    shops = Shop.objects.filter(active = True)
    shop_names = []
    for s in shops:
        shop_names.append(s.name)
    shop_names = json.dumps(shop_names)
    return render_to_response('shops.html', RequestContext(request,locals()))

def get_shops(request):
    results = []
    if request.method == 'POST':
        shop = request.POST.get('shop')
        allShops = Shop.objects.filter(name__icontains = shop)
        for a in allShops:
            if a.active:
                info = {}
                info['name'] = a.name
                info['image'] = a.image.url
                info['ostan'] = a.location.ostan
                info['shahr'] = a.location.shahr
                info['mahale'] = a.location.mahale
                info['website'] = a.website
                info['tel'] = a.tel
                info['id'] = a.id
                info['address'] = a.address
                results.append(info)
    return HttpResponse(json.dumps(results), content_type='application/json')

def institute(request, institute_id):
    institute = Institute.objects.get(id = institute_id)
    return render_to_response('institute.html', RequestContext(request,locals()))

def workshop(request, workshop_id):
    workshop = Workshop.objects.get(id = workshop_id)
    return render_to_response('workshop.html', RequestContext(request,locals()))

def manufacturer(request, manufacturer_id):
    manufacturer = Manufacturer.objects.get(id = manufacturer_id)
    return render_to_response('manufacturer.html', RequestContext(request,locals()))

def new_directory(request):
    if request.method == 'POST':
        if 'manufacturer_submit' in request.POST:
            manu_form = manufacturer_form(request.POST)
            if manu_form.is_valid():
                manufacturer = Manufacturer()
                manu_id = make_manufacturer(manufacturer, manu_form, request)
                return HttpResponseRedirect('/manufacturer/%d/' % manu_id)
        elif 'institute_submit' in request.POST:
            inst_form = institute_form(request.POST)
            if inst_form.is_valid():
                institute = Institute()
                inst_id = make_institute(institute, inst_form, request)
                return HttpResponseRedirect('/institute/%d/' % inst_id)
        elif 'master_submit' in request.POST:
            mast_form = master_form(request.POST)
            if mast_form.is_valid():
                master = Master()
                mast_id = make_master(master, mast_form, request)
                return HttpResponseRedirect('/master/%d/' % mast_id)
        elif 'workshop_submit' in request.POST:
            work_form = workshop_form(request.POST)
            if work_form.is_valid():
                workshop = Workshop()
                work_id = make_workshop(workshop, work_form, request)
                return HttpResponseRedirect('/workshop/%d/' % work_id)
        elif 'shop_submit' in request.POST:
            shop__form = shop_form(request.POST)
            if shop__form.is_valid():
                shop = Shop()
                shop_id = make_shop(shop, shop__form, request)
                return HttpResponseRedirect('/shop/%d/' % shop_id)
    else:
        ostan = Ostan.objects.all()
        manu_form = manufacturer_form()
        inst_form = institute_form()
        mast_form = master_form()
        work_form = workshop_form()
        shop__form = shop_form()
    return render_to_response('new_directory.html', RequestContext(request,locals()))


@csrf_protect
def search_directory(request, directory):
    result = []
    ans = []
    if request.method == 'POST':
        if directory == 'shop':
            ostan = request.POST.get('ostan')
            shahr = request.POST.get('shahr')
            mahale = request.POST.get('mahale')
            category = request.POST.get('saaz')
            name = request.POST.get('min_price')
            if ostan:
                ans = Shop.objects.filter(location__ostan = ostan)
                if shahr:
                    ans = Shop.objects.filter(location__shahr = shahr)
                    if mahale:
                        ans = Shop.objects.filter(location__mahale = mahale)
            if category:
                ans = ans.filter(category__cat1 = category)
            if name:
                ads = ans.filter(name__icontains = name)
            for i in ans:
                info = {}
                info['id'] = i.id
                info['image'] = i.image.url
                info['name'] = i.name
                info['category'] = i.category
                result.append(info)
    return HttpResponse(json.dumps(result), content_type='application/json')




def directories(request):
    category = has_saaz_autocomplete()
    form = directories_form()
    masters = Master.objects.order_by('?')[:5]
    institutes = Institute.objects.order_by('?')[:5]
    shops = Shop.objects.order_by('?')[:5]
    workshops = Workshop.objects.order_by('?')[:5]
    manufacturers = Manufacturer.objects.order_by('?')[:5]
    saaz = request.GET.get('saaz', '')
    if saaz is not '':
        saaz = Instrument.objects.get(name = saaz)
        masters = saaz.masters.all()
        institutes = saaz.institutes.all()
        workshops = saaz.workshops.all()
        manufacturers = saaz.manufacturers.all()
    return render_to_response('directories.html', RequestContext(request,locals()))

@ensure_csrf_cookie
def search(request):
    if request.is_ajax():
        term = request.body[1:len(str(request.body))-2]
    if term == 'masters':
        masterss = Master.objects.order_by('?')[:2]
        return HttpResponse(json.dumps(Masters),content_type='application/json')


def masters_search(request):
    term = request.GET.get("term")
    masters = Master.objects.filter(name__icontains = term)
    if request.GET.get("format") == "json":
        data = []
        for master in masters:
            data.append({"id": master.name })
        return HttpResponse(json.dumps(data), content_type='application/json')

def institutes_search(request):
    term = request.GET.get("term")
    institutes = Institute.objects.filter(name__icontains = term)
    if request.GET.get("format") == "json":
        data = []
        for institute in institutes:
            data.append({"id": institute.name })
        return HttpResponse(json.dumps(data), content_type='application/json')

def saaz_search(request):
    term = request.GET.get("term")
    saazs = Category.objects.filter(cat3__icontains = term)
    if request.GET.get("format") == "json":
        data = []
        for saaz in saazs:
            data.append({"id": saaz.cat3 })
        return HttpResponse(json.dumps(data), content_type='application/json')


def make_manufacturer(m, form, request):
    m.name = form.cleaned_data['name']
    location = Location()
    location.ostan = form.cleaned_data['ostan']
    location.shahr = form.cleaned_data['shahr']
    location.mahale = form.cleaned_data['mahale']
    location.save()
    m.location = location
    m.address = form.cleaned_data['address']
    m.tel = form.cleaned_data['tel']
    m.range_min = form.cleaned_data['range_min']
    m.range_max = form.cleaned_data['range_max']
    m.website = form.cleaned_data['website']
    m.tel = form.cleaned_data['tel']
    m.image = request.FILES['image']
    m.resume = form.cleaned_data['resume']
    m.save()
    instruments = form.cleaned_data['instruments'].split(',')
    for i in instruments:
        instrument = Category.objects.get(cat3 = i)
        if instrument is not None:
            m.instruments.add(instrument)
    return m.id

def make_institute(i, form, request):
    i.name = form.cleaned_data['name']
    location = Location()
    location.ostan = form.cleaned_data['ostan']
    location.shahr = form.cleaned_data['shahr']
    location.mahale = form.cleaned_data['mahale']
    location.save()
    i.location = location
    i.address = form.cleaned_data['address']
    i.tel = form.cleaned_data['tel']
    i.website = form.cleaned_data['website']
    i.tel = form.cleaned_data['tel']
    i.image = request.FILES['image']
    i.logo = request.FILES['logo']
    i.resume = form.cleaned_data['resume']
    masters = form.cleaned_data['masters'].split(',')
    instruments = form.cleaned_data['instruments'].split(',')
    i.save()
    for m in masters:
        master = Master.objects.get(name = m)
        if master is not None:
            i.masters.add(master)
    for s in instruments:
        instrument = Category.objects.get(cat3 = s)
        if instrument is not None:
            i.instruments.add(instrument)


    return i.id

def make_master(m, form, request):
    m.name = form.cleaned_data['name']
    m.method = form.cleaned_data['method']
    m.image = request.FILES['image']
    #m.institutes =
    m.resume = form.cleaned_data['resume']
    m.save()
    institutes = ' '.join(form.cleaned_data['institutes'].split())
    institutes = institutes.split('،')
    m.save()
    instruments = form.cleaned_data['instruments'].split(',')
    institutes = form.cleaned_data['institutes'].split(',')
    for i in institutes:
        institute = Institute.objects.get(name = i)
        if institute is not None:
            m.institutes.add(institute)
    for i in instruments:
        instrument = Category.objects.get(cat3 = i)
        if instrument is not None:
            m.instruments.add(instrument)
    return m.id

def make_workshop(w, form, request):
    w.name = form.cleaned_data['name']
    location = Location()
    location.ostan = form.cleaned_data['ostan']
    location.shahr = form.cleaned_data['shahr']
    location.mahale = form.cleaned_data['mahale']
    location.save()
    w.location = location
    w.address = form.cleaned_data['address']
    w.tel = form.cleaned_data['tel']
    w.website = form.cleaned_data['website']
    w.tel = form.cleaned_data['tel']
    w.image = request.FILES['image']
    w.resume = form.cleaned_data['resume']
    w.save()
    instruments = form.cleaned_data['instruments'].split(',')
    for i in instruments:
        instrument = Category.objects.get(cat3 = i)
        if instrument is not None:
            w.instruments.add(instrument)
    return w.id

def make_shop(s, form, request):
    s.name = form.cleaned_data['name']
    location = Location()
    location.ostan = form.cleaned_data['ostan']
    location.shahr = form.cleaned_data['shahr']
    location.mahale = form.cleaned_data['mahale']
    location.save()
    s.location = location
    s.address = form.cleaned_data['address']
    s.tel = form.cleaned_data['tel']
    s.website = form.cleaned_data['website']
    s.tel = form.cleaned_data['tel']
    s.image = request.FILES['image']
    s.resume = form.cleaned_data['resume']
    saaz = Category()
    saaz.cat1 = form.cleaned_data['directory_shop_sub1']
    saaz.save()
    s.category = saaz
    s.save()
    return s.id