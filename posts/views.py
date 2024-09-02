from django.shortcuts import render
from .models import Posts
from django.contrib.auth.decorators import login_required


# Create your views here.
def posts_list(request):
    posts = Posts.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts})

def post_page(request, slug):
    posts = Posts.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', { 'post': posts})

@login_required(login_url="/users/login/")
def post_new(request):
    return render(request, 'posts/post_new.html')