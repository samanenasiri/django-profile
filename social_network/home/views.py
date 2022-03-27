from django.shortcuts import render
from django.views import View
from .models import Post


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'home/index.html', {'posts': posts})


class PostDetailView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        return render(request, "home/detail.html", {'post': post})

# Create your views here.
