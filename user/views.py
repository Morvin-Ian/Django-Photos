from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from user.models import Post, Profile
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.models import User

from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# @login_required
# def index(request):
   
#     posts = Post.objects.all()
#     profiles = Profile.objects.all()
  
#     return render(request,'user/index.html', {"posts":posts,"profiles":profiles})

class IndexView(LoginRequiredMixin,ListView): 
    model = Post
    context_object_name= 'posts'
    template_name = 'user/index.html'
    ordering = ['-time']


# @login_required
# def detail(request, id):
#     details = Post.objects.get(id=id)

#     return render(request,'user/detail.html',{"details":details})


class PostDetailView(DetailView): 
    model = Post
    context_object_name= 'details'
    template_name = 'user/detail.html'

class PostCreateView(LoginRequiredMixin,CreateView): 
    model = Post
    fields = ['caption', 'image']
    template_name = 'user/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
  

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): 
    model = Post
    fields = ['caption', 'image']
    template_name = 'user/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True 
        else:
            False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): 
    model = Post
    fields = ['caption', 'image']
    template_name = 'user/confirm.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True 
        else:
            False



