from django import forms

class directories_form(forms.Form):
    saaz = forms.CharField(required= False)

class manufacturer_form(forms.Form):
    name = forms.CharField(required = False)
    ostan = forms.CharField(required = False)
    shahr = forms.CharField(required = False)
    mahale = forms.CharField(required = False)
    address = forms.CharField(required = False)
    tel = forms.CharField(required = False)
    range_min = forms.IntegerField(required = False) # edit
    range_max = forms.IntegerField(required = False) # edit
    website = forms.CharField(required = False)
    image = forms.FileField(required = False)
    resume = forms.CharField(required = False)
    directory_manufacturer_sub1 = forms.CharField(required = False)
    directory_manufacturer_sub2 = forms.CharField(required = False)
    directory_manufacturer_sub3 = forms.CharField(required = False)
    directory_manufacturer_sub4 = forms.CharField(required = False)

class shop_form(forms.Form):
    name = forms.CharField(required = False)
    directory_shop_sub1 = forms.CharField(required = False) # bazbini she
    ostan = forms.CharField(required = False)
    shahr = forms.CharField(required = False)
    mahale = forms.CharField(required = False)
    address = forms.CharField(required = False)
    tel = forms.CharField(required = False)
    website = forms.CharField(required = False)
    image = forms.FileField(required = False)
    resume = forms.CharField(required = False)

class shop_search(forms.Form):
    name = forms.CharField(required=False)
    location = forms.CharField(required=False)
    cat = forms.CharField(required=False)

class workshop_form(forms.Form):
    name = forms.CharField(required = False)
    directory_workshop_sub1 = forms.CharField(required = False)
    directory_workshop_sub2 = forms.CharField(required = False)
    directory_workshop_sub3 = forms.CharField(required = False)
    directory_workshop_sub4 = forms.CharField(required = False)
    ostan = forms.CharField(required = False)
    shahr = forms.CharField(required = False)
    mahale = forms.CharField(required = False)
    address = forms.CharField(required = False)
    tel = forms.CharField(required = False)
    website = forms.CharField(required = False)
    image = forms.FileField(required = False)
    resume = forms.CharField(required = False)

class institute_form(forms.Form):
    name = forms.CharField(required = False)
    instruments = forms.CharField(required = False) # bazbini she
    masters = forms.CharField(required= False)
    ostan = forms.CharField(required = False)
    shahr = forms.CharField(required = False)
    mahale = forms.CharField(required = False)
    address = forms.CharField(required = False)
    tel = forms.CharField(required = False)
    website = forms.CharField(required = False)
    image = forms.FileField(required = False)
    logo = forms.FileField(required = False)
    resume = forms.CharField(required = False)


class master_form(forms.Form):
    name= forms.CharField(required = False)
    instruments= forms.CharField(required = False)
    method = forms.CharField(required = False)
    institutes = forms.CharField(required = False)
    image = forms.FileField(required = False)
    resume = forms.CharField(required = False)