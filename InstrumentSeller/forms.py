# -*- coding: utf-8 -*-
from django import forms

class ad_form(forms.Form):
    title = forms.CharField()
    details = forms.CharField()
    model = forms.CharField()
    manufacturer = forms.CharField()
    transport= forms.CharField()
    returning = forms.CharField()
    purchase = forms.CharField()
    price = forms.IntegerField()
    year = forms.ChoiceField(choices=[(x, x) for x in range(1370, 1393)], required=False)
    used = forms.BooleanField(required= False)
    sound = forms.FileField(required=False)
    img1 = forms.FileField(required= False)
    img2 = forms.FileField(required=False)
    img3 = forms.FileField(required=False)
    img4 = forms.FileField(required=False)
    img5 = forms.FileField(required=False)
    img6 = forms.FileField(required=False)
    sell_ostan = forms.CharField()
    sell_shahr = forms.CharField()
    sell_mahale = forms.CharField()
    saaz = forms.CharField()
    show_email = forms.BooleanField(required= False)
    show_tel = forms.BooleanField(required= False)

class profile_form1(forms.Form):
    email = forms.EmailField(required= False)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

class profile_form2(forms.Form):
    name = forms.CharField(required= False)
    family_name = forms.CharField(required= False)
    tel = forms.CharField(required= False)
    def clean(self):
       return self.cleaned_data

class profile_form3(forms.Form):
    permission = forms.ChoiceField(choices=(('True', 'بله'),('False', 'خیر')))

class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class register_form(forms.Form):
    first_name= forms.CharField()
    family_name = forms.CharField()
    email = forms.EmailField()
    pass1 = forms.CharField(widget=forms.PasswordInput)
    pass2 = forms.CharField(widget=forms.PasswordInput)

class offer_form(forms.Form):
    sender = forms.CharField()
    transport = forms.CharField()
    email = forms.EmailField()
    tel = forms.IntegerField()
    content = forms.CharField()
    price= forms.IntegerField()
    is_offer = forms.BooleanField(required= False)

class home_search_form(forms.Form):
    home_ostan = forms.CharField(required= False)
    home_shahr= forms.CharField(required= False)
    home_mahale = forms.CharField(required= False)
    saaz = forms.CharField(required= False)
    min_price = forms.CharField(required= False)
    max_price = forms.CharField(required= False)
