from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def Index(request):
    posts = Post.objects.all()
    return render(request,"app/index.html",{'posts':posts})

def Likepost(request):
    if request.method=="GET":
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id) 