from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

# Create your models here.

class Location(models.Model):
    city = models.ForeignKey('City')
    neighborhood= models.CharField(max_length=100)
    
class Advertisement(models.Model):
    title = models.CharField(max_length = 200)
    user = models.ForeignKey('User_Profile')
    location = models.ForeignKey(Location, blank = True, null = True)
    submit_date= models.DateTimeField(auto_now=True)
    price= models.IntegerField()
    advertisement_type = models.CharField(max_length=50) # doroste?
    details = models.CharField(max_length=500, blank = True)
    transport = models.CharField(max_length=100, blank = True)
    purchase = models.CharField(max_length=100, blank = True)
    returning = models.CharField(max_length=100, blank = True)
    sound = models.FileField(upload_to = 'instrument_sound', blank = True)
    image= models.ForeignKey('Ad_Image', null = True)
    used = models.CharField(max_length=20)
    instrument = models.ForeignKey('Instrument')
    def __str__(self):
        return self.instrument.name
    
class Ad_Image(models.Model):
    image = models.FileField(upload_to = 'ad_pics')
    ad = models.ForeignKey(Advertisement, related_name= 'images', null = True, blank = True)
    
    
class User_Profile(models.Model):
    user = models.ForeignKey(User)
    tel = models.IntegerField(blank = True, null = True)
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
    manufacturer = models.CharField(max_length = 200, blank = True)
    used = models.BooleanField()
    model = models.CharField(max_length = 50)
    year = models.IntegerField()
    def __str__(self):
        return self.name
    
class Offer(models.Model):
    content = models.CharField(max_length=500)
    time = models.DateTimeField()
    price= models.IntegerField()
    ad= models.ForeignKey(Advertisement)
    
class Property(models.Model):
    instrument = models.ForeignKey(Instrument)
    feature = models.CharField(max_length=100)
    
class Property_Value(models.Model):
    propertys = models.ForeignKey(Property)
    value = models.IntegerField()
    
class State(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length = 100)
    state= models.ForeignKey(State, related_name ='cities')
    def __str__(self):
        return self.name
