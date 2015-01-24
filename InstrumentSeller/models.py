from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import ImageField
from Directory.models import *
# Create your models here.

class Ostan(models.Model):
    name = models.CharField(max_length= 50)
    def __str__(self):
        return self.name

class Shahr(models.Model):
    name = models.CharField(max_length=50)
    ostan = models.ForeignKey(Ostan, blank = True, null = True )
    def __str__(self):
        return self.name

class Mahale(models.Model):
    name = models.CharField(max_length=100)
    shahr = models.ForeignKey(Shahr, blank = True, null = True )
    def __str__(self):
        return self.name

class Location(models.Model):
    ostan= models.CharField(max_length=100)
    shahr= models.CharField(max_length=100, blank = True, null = True)
    mahale= models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.mahale

class Category(models.Model):
    cat1 = models.CharField(max_length=50,)
    cat2 = models.CharField(max_length=50, null=True, blank=True)
    cat3 = models.CharField(max_length=50, null=True, blank=True)
    cat4 = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        if self.cat4:
            return self.cat4
        elif self.cat3:
            return self.cat3
        elif self.cat2:
            return self.cat2
        else:
            return self.cat1

class Advertisement(models.Model):
    title = models.CharField(max_length = 200)
    user = models.ForeignKey('User_Profile', related_name='Ads', null= True)
    location = models.ForeignKey(Location, blank = True, null = True)
    submit_date= models.DateTimeField(auto_now=True)
    price= models.IntegerField()
    type = models.IntegerField(default=0) # 0 == active , 1 == deleted , 2 == sold
    details = models.CharField(max_length=500, blank = True)
    transport = models.CharField(max_length=100, blank = True)
    purchase = models.CharField(max_length=100, blank = True)
    returning = models.CharField(max_length=100, blank = True)
    sound = models.FileField(upload_to = 'instrument_sound', blank = True)
    image= models.ForeignKey('Ad_Image', null = True)
    instrument = models.ForeignKey('Instrument', related_name='ad')
    offer = models.BooleanField(default= True)
    show_email = models.BooleanField(default= True)
    show_tel = models.BooleanField(default= True)
    def __str__(self):
        return self.title
    
class Ad_Image(models.Model):
    image = models.FileField(upload_to = 'ad_pics')
    ad = models.ForeignKey(Advertisement, related_name= 'images', null = True, blank = True)
    
    
class User_Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    tel = models.CharField(max_length=20,blank = True, null = True)
    image = models.FileField(upload_to='profile_images', blank = True)
    score = models.IntegerField(default = 0)
    allowed_ad_count = models.IntegerField()
    favorite = models.ManyToManyField(Advertisement, related_name="favorit_users", blank = True)
    view = models.ManyToManyField(Advertisement, related_name="view_users", blank = True)
    location = models.ForeignKey(Location, blank = True, null = True)
    def __str__(self):
        return self.user.first_name

class Instrument(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey('Directory.Manufacturer', null = True, related_name='Instruments')
    used = models.BooleanField(default = False)
    model = models.CharField(max_length = 50)
    year = models.IntegerField()
    category = models.ForeignKey('Category', null=True)
    def __str__(self):
        return self.name
    
class Offer(models.Model):
    sender = models.CharField(max_length=200)
    transport = models.CharField(max_length=300, blank = True, null = True)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now=True)
    price= models.IntegerField(blank = True, null = True)
    ad= models.ForeignKey(Advertisement, related_name='offers')
    read = models.BooleanField(default= False)
    is_offer = models.BooleanField(default= True)
