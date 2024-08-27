from django.shortcuts import render
from .models import Posts

# Create your views here.
def posts_list(request):
    posts = Posts.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts})

