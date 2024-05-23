from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib import messages
from .decorators import login_required

from .models import *
from .forms import *

# Create your views here.
def register(request):
    mes=None
    user=None

    if request.user.is_authenticated:
        return redirect ('home')
    
    form =RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)

            messages.success(request, f'{user} you created your profile')
            return redirect('home')
        
        else:
            mes=messages.error(request, f'{user} you entered something wrong')
            # return redirect('home')
    return render(request, 'space/register.html', {'form': form, 'mes': mes})

def user_login(request):
    posts= Post.objects.all()
    mes= None

    if request.user.is_authenticated:
        return redirect ('home')
    
    form=LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                mes= messages.success(request, f'{username} you entered your working space!')
                return redirect('home')
        else:
            mes= messages.error(request, f'{username} or password are wrong')

    return render(request, 'space/login.html', {'form': form, 'posts': posts, 'mes': mes})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('home')

@login_required()
def user_profile(request):  
    
    form = ProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileForm(instance=request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'{request.user.username} your profile has been updated')
            return redirect('home')
    
    return render(request, 'space/profile.html', {'form': form})

def index(request):
    posts=Post.objects.all()
    tags = Tag.objects.all()
    search_res =''
    user= UserProfile

    
    selected_tag = request.GET.get('option')

    if selected_tag:
        posts = posts.filter(tags__id=selected_tag)
        print(posts)
    
    search_res = request.GET.get('search')
    
    if search_res:
        posts = posts.filter(title__icontains = search_res)
        print(posts)

    if request.method == 'POST':
        form=CreateTitleForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            posts = Post.objects.create(title=title)
            posts.save()
            return redirect('create')
            
    else:
        form=CreateTitleForm()
        
    paginator = Paginator(posts, 4)
    page=int(request.GET.get('page', 1))
    posts=paginator.get_page(page)
    return render(request, 'space/index.html', {'form': form, 'posts': posts, 'tags': tags, 'user': user})

@login_required()
def create(request):
    mes = None
    tags = Tag.objects.all()
    init_data = {}
    first = Post.objects.first()

    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            content = form.cleaned_data['content']
            tags = form.cleaned_data['tags']

            if first:
                first.title = title
                first.image = image
                first.content = content
                first.tags.set(tags)
                first.save()
            else:
                new_post = Post.objects.create(title=title, image=image, content=content)
                new_post.tags.set(tags)
            
            messages.success(request, f'Post "{title}" has been created')
            return redirect('home')
        mes=messages.error(request, 'Post created')
    else:
        if first:
            init_data = {
                'title': first.title,
                'image': first.image,
                'content': first.content,
                'tags': first.tags.all()
            }
        form = CreatePostForm(initial=init_data)

    return render(request, 'space/create.html', {'form': form, 'mes': mes, 'tags': tags})

@login_required()
def edit(request, post_id):
    post_id=int(post_id)
    post=get_object_or_404(Post, id=post_id)
    

    if request.method == 'POST':
        print('posting')
        tag_ids=list(map(int, request.POST.getlist('tags')))
        tags=Tag.objects.filter(id__in=tag_ids)
        image=request.FILES.get('image')
        if image:
            post.image.save(image.name, image)
        post.tags.clear()
        post.tags.add(*tags)
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.tags.set(tags)
        post.save()
        messages.success(request, f'Post "{post}" has been deleted')

        return redirect('home')
    
    tags=Tag.objects.all()

    return render(request, 'space/edit.html', {'post': post, 'tags': tags})

@login_required()
def delete(request, post_id):
    post_id=int(post_id)
    post=get_object_or_404(Post, id=post_id)
    tags=Tag.objects.all()
    post.delete()
    messages.warning(request, f'Post "{post}" has been deleted')
    return redirect('home')

def post(request, post_id):
    post = Post.objects.get(pk=post_id)

    return render(request, 'space/post.html', {'post': post})

def view_tags(request, tag_id):

    post=Post.objects.all()
    tags=Tag.objects.filter(id=tag_id)

    return render(request, 'space/index.html', {'post': post, 'tags': tags})