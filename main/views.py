from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
#from django.contrib.auth.decorators import login_required
# Create your views here.

from main.models import Post

# Create your views here.

#@login_required(login_url='/log')
def home(request):
    context = RequestContext(request)
    posts = Post.objects.all()
    context['usuario_actual'] = request.user
    context['posts'] = posts
    #for p in posts : print posts
    return render_to_response("home.html", context)

def article(request,id_post):
    context = RequestContext(request)
    post = Post.objects.get(pk=id_post)
    context['post'] = post
    return render_to_response("post.html", context)
