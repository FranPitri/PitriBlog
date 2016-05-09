from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.

from main.models import Post

# Create your views here.

def home(request):
    context = RequestContext(request)
    posts = Post.objects.all()
    context['usuario_actual'] = request.user
    context['posts'] = posts
    return render_to_response("hello.html", context)
