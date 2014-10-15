from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

# Create your models here.

class Location(models.Model):
    city = models.ForeignKey('City')
    neighborhood= models.CharField(max_length=100)
    
class Advertisement(models.Model):
    user = models.ForeignKey('User_Profile')
    location = models.ForeignKey(Location)
    property_value = models.ForeignKey('Property_Value')
    submit_date= models.DateTimeField()
    price= models.IntegerField()
    advertisement_type = models.CharField(max_length=50) # doroste?
    details = models.CharField(max_length=500)
    transport = models.CharField(max_length=100)
    purchase = models.CharField(max_length=100)
    returning = models.CharField(max_length=100)
    sound = models.FileField(upload_to = 'instrument_sound')
    image= models.ForeignKey('Ad_Image')
    instrument = models.ForeignKey('Instrument')
    
class Ad_Image(models.Model):
    image = models.FileField(upload_to = 'ad_pics')
    ad = models.ForeignKey(Advertisement, related_name= 'images')
    
    
class User_Profile(models.Model):
    user = models.ForeignKey(User)
    tel = models.IntegerField()
    image = models.FileField(upload_to='profile_images')
    score = models.IntegerField(default = 0)
    allowed_ad_count = models.IntegerField()
    favorite = models.ManyToManyField(Advertisement, related_name="favorit_users")
    view = models.ManyToManyField(Advertisement, related_name="view_users")
    location = models.ForeignKey(Location)
    

class Instrument(models.Model):
    name = models.CharField(max_length=50)
    feature1 = models.CharField(max_length=100)
    feature2 = models.CharField(max_length=100)
    
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
    
class City(models.Model):
    name = models.CharField(max_length = 100)
    state= models.ForeignKey(State, related_name ='cities')
    
