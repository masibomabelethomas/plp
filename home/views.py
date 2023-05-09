from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# Create your views here.

def home_view(request):

    posts = Post.objects.all()
    context={
        "articles": posts
    }
    return render(request, "home.html", context)
