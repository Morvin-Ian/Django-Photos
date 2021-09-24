from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user.models import Post, Profile
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.models import User


@login_required
def index(request):
   
    posts = Post.objects.all()
    profiles = Profile.objects.all()
  
    return render(request,'user/index.html', {"posts":posts,"profiles":profiles})

@login_required
def detail(request, id):
    details = Post.objects.get(id=id)

    return render(request,'user/detail.html',{"details":details})

def create(request):
    if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                return redirect('home-page')

    else:
        form = PostForm()
    return render(request,'user/create.html', {"form":form})
