# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render
from InstrumentSeller.models import *
from InstrumentSeller.forms import *
from django.contrib.auth.models import User


def home(request):
    mainAds = Advertisement.objects.all()
    ad = Advertisement.objects.all()
    return render(request,'home.html', locals())

@csrf_protect
def sell(request):
    if request.method == 'POST':    
        form = ad_form(request.POST, request.FILES)
        if form.is_valid():
            saaz = Instrument()
            ad = Advertisement()
            saaz.name = "sample"
            saaz.manufacturer = form.cleaned_data['manufacturer']
            saaz.model = form.cleaned_data['model']
            saaz.year = form.cleaned_data['year']
            saaz.save()
            user = User_Profile()
            user.user = User.objects.get(id = 1)
            user.allowed_ad_count = 2
            user.save()
            img1 = Ad_Image(image = request.FILES['img1'])
            img1.save()
            img2 = Ad_Image(image = request.FILES['img2'])
            img2.save()
            img3 = Ad_Image(image = request.FILES['img3'])
            img3.save()
            img4 = Ad_Image(image = request.FILES['img4'])
            img4.save()
            img5 = Ad_Image(image = request.FILES['img5'])
            img5.save()
            img6 = Ad_Image(image = request.FILES['img6'])
            img6.save()
            ad.images.add(img1)
            ad.images.add(img2)
            ad.images.add(img3)
            ad.images.add(img4)
            ad.images.add(img5)
            ad.images.add(img6)
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
            ad.sound = request.FILES['sound']
            ad.save()
    else:
        form = ad_form()
    return render_to_response('sell.html', RequestContext(request,locals()))

def profile(request):
    return render(request, 'profile.html')

def profile_listing(request):
    return render(request, 'profile_listing.html')

def profile_messages(request):
    return render(request, 'profile_messages.html')

def profile_show_message(request):
    return render(request, 'profile_show_message.html')

def profile_invoices(request):
    return render(request, 'profile_invoices.html')

def profile_settings(request):
    return render(request, 'profile_settings.html')

def compare(request):
    return render(request, 'compare.html')

def instrument(request):
    return render(request, 'instrument.html')

def temp(request):
    return render(request, 'temp.html')