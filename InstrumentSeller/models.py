from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

# Create your models here.

class Location(models.Model):
    ostan= models.CharField(max_length=100)
    shahr= models.CharField(max_length=100)
    mahale= models.CharField(max_length=100)
    def __str__(self):
        return self.mahale

class Category(models.Model):
    cat1 = models.CharField(max_length=50)
    cat2 = models.CharField(max_length=50)
    cat3 = models.CharField(max_length=50)
    cat4 = models.CharField(max_length=50)
    def __str__(self):
        return self.cat4

class Advertisement(models.Model):
    title = models.CharField(max_length = 200)
    user = models.ForeignKey('User_Profile', related_name='Ads')
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
    used = models.CharField(max_length=20)
    instrument = models.ForeignKey('Instrument', related_name='ad')
    def __str__(self):
        return self.title
    
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
    category = models.ForeignKey(Category, null=True)
    def __str__(self):
        return self.name
    
class Offer(models.Model):
    sender = models.ForeignKey(User_Profile)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now=True)
    price= models.IntegerField()
    ad= models.ForeignKey(Advertisement, related_name='offers')
    read = models.BooleanField(default= False)
    
class Property(models.Model):
    instrument = models.ForeignKey(Instrument)
    feature = models.CharField(max_length=100)
    
class Property_Value(models.Model):
    propertys = models.ForeignKey(Property)
    value = models.IntegerField()
