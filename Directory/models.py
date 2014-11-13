from django.db import models
from InstrumentSeller.models import *
# Create your models here.
class Master(models.Model):
    name= models.CharField(max_length= 100)
    instruments= models.ManyToManyField(Instrument, related_name='masters', null= True, blank= True)
    method = models.CharField(max_length= 100, null= True, blank= True)
    institutes = models.ManyToManyField('Institute', related_name='masters', null= True, blank= True)
    image = models.FileField(upload_to='masters', null= True, blank= True)
    resume = models.CharField(max_length=500, null= True, blank= True)
    active = models.BooleanField(default= False)
    def __str__(self):
        return self.name

class Institute(models.Model):
    name = models.CharField(max_length= 200)
    location = models.ForeignKey(Location)
    instruments = models.ManyToManyField(Instrument, related_name='institutes', null= True, blank= True)
    address = models.CharField(max_length=200)
    tel= models.CharField(max_length=100)
    website = models.CharField(max_length=400, null= True)
    logo = models.FileField(upload_to='institute_logos', null= True)
    image = models.FileField(upload_to='institute_images', null= True)
    resume = models.CharField(max_length= 500, null= True)
    active = models.BooleanField(default= False)
    def __unicode__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length= 200)
    instrument= models.ForeignKey(Instrument, related_name='manufacturers')
    location = models.ForeignKey(Location)
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=100)
    #range = models.CharField(max_length=100, null= True) # edit
    range_min = models.IntegerField()
    range_max = models.IntegerField()
    website = models.CharField(max_length=400, null= True)
    image = models.FileField(upload_to='manufacturers', null= True)
    resume = models.CharField(max_length=400, null= True)
    active = models.BooleanField(default= False)
    def __unicode__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length= 200)
    location = models.ForeignKey(Location)
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=100)
    website = models.CharField(max_length=400, null= True)
    category = models.ForeignKey(Category, related_name='shops')
    image = models.FileField(upload_to='shops', null= True)
    resume = models.CharField(max_length=400, null= True)
    active = models.BooleanField(default= False)
    def __unicode__(self):
        return self.name

class Workshop(models.Model):
    name = models.CharField(max_length= 200)
    location = models.ForeignKey(Location)
    address = models.CharField(max_length=200)
    instrument = models.ForeignKey(Instrument, related_name='workshops')
    tel = models.CharField(max_length=100)
    website = models.CharField(max_length=400, null= True)
    image = models.FileField(upload_to='workshops', null= True)
    resume = models.CharField(max_length=400, null= True)
    active = models.BooleanField(default= False)
    def __unicode__(self):
        return self.name

class Course(models.Model):
    master= models.ForeignKey(Master, null= True, blank= True)
    institute = models.ForeignKey(Institute, null= True, blank= True)
    class_time = models.CharField(max_length=300) # chejuri bayad bashe?