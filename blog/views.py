from django.shortcuts import render
from .models import Blogpost

def blog(request):
  posts = Blogpost.objects.all()
  context = {'posts':posts}
  return render(request, 'blog/index.html', context)

def blogpost(request, id):
  post = Blogpost.objects.filter(postId = id)[0]

  context = {'post': post}
  return render(request, 'blog/post.html', context)