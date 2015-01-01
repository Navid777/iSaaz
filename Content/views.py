# -*- coding: utf-8 -*-
# Create your views here.

from Content.models import *
from InstrumentSeller.models import *
from django.contrib import auth
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from Content.forms import *
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import json
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import get_object_or_404
import inspect

def log(error):
    frame, filename, ln, fn, lolc, idx = inspect.getouterframes(inspect.currentframe())[1]
    print ("Error: " + error + " " + filename, ln, fn)

def has_saaz_autocomplete():
    category = []
    for c in Category.objects.all():
        category.append(c.cat4)
    return category

def articles(request):
    log("articles")
    category = has_saaz_autocomplete()
    articles = Article.objects.all()
    return render_to_response('articles.html', RequestContext(request,locals()))

@csrf_protect
def article_search(request):
    mainArts = []
    if request.method == 'POST':
            saaz = request.POST.get('saaz')
            arts = Article.objects.filter(category__cat4 = saaz)
            for article in arts:
                #info = serializers.serialize('json', [article, ] )
                info = model_to_dict(article)
                info['image'] = article.image.url
                mainArts.append(info)
    return HttpResponse(json.dumps(mainArts), mimetype='application/javascript')


@csrf_protect
def view_article(request, art_id):
    print("view_article")
    category = has_saaz_autocomplete()
    context = RequestContext(request)
    article = Article.objects.get(id = art_id)
    if request.method == 'POST':
        if request.is_ajax():
            if 'comment' in request.POST:
                reply = Sub_Comment()
                reply.name = request.POST.get('name')
                reply.email = request.POST.get('email')
                reply.content = request.POST.get('content')
                reply.comment = Comment.objects.get(id = request.POST.get('comment'))
                reply.save()
                info = model_to_dict(reply)
                info['comment'] = reply.comment.id
                return HttpResponse(json.dumps(info), mimetype='application/javascript')
            else:
                comment = Comment()
                comment.name = request.POST.get('name')
                comment.email = request.POST.get('email')
                comment.content = request.POST.get('content')
                comment.article = article
                comment.save()
                info = model_to_dict(comment)
                return HttpResponse(json.dumps(info), mimetype='application/javascript')
    cform = comment_form()
    rform = comment_form()
    return render_to_response('article.html', RequestContext(request,locals()))

def search_by_category(request, category_name):
    all_article = Article.objects.all()
    articles = []
    for i in all_article:
        if i.category.cat4 == category_name:
            articles.append(i)
    return render(request, 'articles.html', locals())

@csrf_protect
def like_article(request):
    likes = 0
    if request.method == 'POST':
        user = request.user
        article_id = request.POST.get('article_id')
        article = Article.objects.get(id = int(str(article_id)))
        user.profile.article_likes.add(article)
        likes = article.likes.count()
    return HttpResponse(json.dumps(likes), mimetype='application/javascript')

@csrf_protect
def comment_like(request):
    info = []
    if request.method == 'POST':
        user = request.user.profile
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id = int(str(comment_id)))
        comment.likes.add(user)
        info.append(comment.id)
        info.append(comment.likes.count())
    return HttpResponse(json.dumps(info), mimetype='application/javascript')

