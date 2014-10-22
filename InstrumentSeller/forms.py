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
    USED = (
        ('used', 'دست دو'),
        ('new', 'جدید')
    )
    used = forms.ChoiceField(choices=USED, required=True)
    sound = forms.FileField(required=False)
    img1 = forms.FileField()
    img2 = forms.FileField(required=False)
    img3 = forms.FileField(required=False)
    img4 = forms.FileField(required=False)
    img5 = forms.FileField(required=False)
    img6 = forms.FileField(required=False)
    ostan = forms.CharField()
    shahr = forms.CharField()
    mahale = forms.CharField()
    sub1 = forms.CharField()
    sub2 = forms.CharField()
    sub3 = forms.CharField()
    sub4 = forms.CharField() #instrument

class profile_form1(forms.Form):
    email = forms.EmailField( required= False)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

class profile_form2(forms.Form):
    name = forms.CharField(required= False)
    family_name = forms.CharField(required= False)
    tel = forms.IntegerField(required= False)
    def clean(self):
       return self.cleaned_data

class profile_form3(forms.Form):
    permission = forms.ChoiceField(choices=(('True', 'بله'),('False', 'خیر')))

class login_form(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()