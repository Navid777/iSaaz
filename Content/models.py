from django.db import models
from InstrumentSeller.models import *

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length= 200)
    content = models.CharField(max_length=2000)
    image = models.FileField(upload_to='articles')
    template = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    translator = models.CharField(max_length= 100 , null = True)
    source = models.CharField(max_length=300, null= True, blank= True)
    time = models.DateTimeField(auto_now= True)
    category = models.ForeignKey(Category, null= True)
    likes = models.ManyToManyField(User_Profile, related_name='article_likes', null= True, blank= True)
    views = models.ManyToManyField(User_Profile, related_name='article_views', null= True, blank= True)
    tags = models.ManyToManyField('Tag', null= True, blank= True)
    related_articles = models.ManyToManyField('Article', null= True, blank= True)
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.CharField(max_length= 300)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    article = models.ForeignKey('Article', related_name="comments", null= True, blank= True)
    likes = models.ManyToManyField(User_Profile, null= True, blank= True)
    #time = models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.name

class Sub_Comment(models.Model):
    comment = models.ForeignKey(Comment, related_name='sub_comments', null= True, blank= True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    #time = models.DateTimeField(auto_now= True)
    likes = models.ManyToManyField(User_Profile, null= True)


