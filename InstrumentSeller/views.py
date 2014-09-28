# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def sell(request):
    return render(request, 'sell.html')

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