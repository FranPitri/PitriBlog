from django.shortcuts import render, render_to_response, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import RequestContext
#from django.contrib.auth.decorators import login_required
# Create your views here.

from main.models import Post
from main.models import Comment
from main.models import Author
from django.contrib.auth.models import User

# Create your views here.

#@login_required(login_url='/log')
def home(request):
    context = RequestContext(request)
    # paginator..
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    
    context['usuario_actual'] = request.user
    context['posts'] = posts
    return render_to_response("home.html", context)

def article(request,id_post):
    post = Post.objects.get(pk=id_post)
    if request.method == 'POST':
        content = request.POST['comment-content']
        comment = Comment()
        comment.author = User.objects.get(pk = request.user.id)
        comment.post = post
        comment.content = content
        comment.approved = True
        comment.save()
    context = RequestContext(request)
    comments = Comment.objects.filter(post=post)
    context['post'] = post
    context['comments'] = comments
    return render_to_response("post.html", context)

def newpost(request):
    context = RequestContext(request)
    if request.method == 'POST':
        Post.objects.create(
                title = request.POST['title'],
                content = request.POST['content'],
                image = request.FILES['image'],
                author = Author.objects.get(user = request.user),
                publicated = True
            )
        
        return redirect("main:home")
    
    return render_to_response("createarticle.html",context)