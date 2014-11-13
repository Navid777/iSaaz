# Create your views here.

from Content.models import  *
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
from django.utils import simplejson
from django.shortcuts import get_object_or_404

def articles(request):
    user = User_Profile.objects.get(user = request.user)
    articles = Article.objects.all()
    return render_to_response('articles.html', RequestContext(request,locals()))

@csrf_protect
def view_article(request, art_id):
    context = RequestContext(request)
    article = Article.objects.get(id = art_id)
    user = User_Profile.objects.get(user = request.user)
    if request.method == 'POST':
        if 'commenting' in request.POST:
            cform = comment_form(request.POST)
            if cform.is_valid():
                comment = Comment()
                comment.name = cform.cleaned_data['name']
                comment.email = cform.cleaned_data['email']
                comment.content = cform.cleaned_data['content']
                comment.article = article
                comment.save()
        else:
            for c in article.comments.all():
                if 'replying' + str(c.id) in request.POST:
                    rform = comment_form(request.POST)
                    if rform.is_valid():
                        reply = Sub_Comment()
                        reply.name = rform.cleaned_data['name']
                        reply.email = rform.cleaned_data['email']
                        reply.content = rform.cleaned_data['content']
                        reply.comment = c
                        reply.save()
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

def like_article(request):
    vars = {}
    if request.method == 'POST':
        user = request.user
        article_id = request.POST.get('article_id', None)
        #article = get_object_or_404(Article, slug=slug)
        article = Article.objects.get(id = int(article_id))
        article.likes.add(user)
        article.save()
    return HttpResponse(simplejson.dumps(vars), mimetype='application/javascript')

def comment_like(request, user_id, comment_id):
    user = User_Profile.objects.get(id = user_id)
    comment = Comment.objects.get(id = comment_id)
    comment.likes.add(user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))