# trips/views.py

from django.shortcuts import render , redirect, get_object_or_404
from .models import Post
from django.contrib import auth
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        user = request.user
        if post.author != user:
            return redirect('post_detail', pk=post.pk)
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('/home/' + str(new_post.pk))

    form = PostForm()
    return render(request, 'create_post.html', {'form': form})


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'location']


@login_required
def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })


@login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'login.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.user.is_authenticated():
        return render(request, 'home.html')

    if request.method == 'POST':

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            print("logged in")
            auth.login(request, user)
            return redirect('home')
        if user is None:
            error = "Invalid username or password. Please try again."
            print("1")
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'welcome.html')


def welcome(request):
    return render(request, 'welcome.html')
