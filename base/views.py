from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import PostForm, UserForm, MyUserCreationForm
from .models import Post, Message, User

# Create your views here.


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('hive')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exists')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('hive')

        else:
            messages.error(request, 'Username or password does not exists')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('main')


def registerUser(request):
    form = MyUserCreationForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        return redirect('hive')

    else:
        messages.error(request, 'An Error occured during registration')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)


def mainPage(request):
    return render(request, 'base/main.html')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(
        Q(description__icontains=q)
    )

    post_count = posts.count()

    context = {'posts': posts, 'post_count': post_count}
    return render(request, 'base/hive.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    post_messages = post.message_set.all().order_by('-created')
    participants = post.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            post=post,
            body=request.POST.get('body'),
        )
        post.participants.add(request.user)
        return redirect('post', pk=post.id)

    context = {'post': post, 'post_messages': post_messages,
               'participants': participants}
    return render(request, 'base/post.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    posts = user.post_set.all()
    post_messages = user.message_set.all()

    context = {'user': user, 'posts': posts, 'post_messages': post_messages}
    return render(request, 'base/profile.html', context)


def editProfile(request, pk):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    context = {'form': form}
    return render(request, 'base/edit-profile.html', context)


@login_required(login_url='login')
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            host = request.user
            post = form.save(commit=False)
            post.host = host
            post.save()
            form.save_m2m()
            return redirect('hive')

    context = {'form': form}
    print(context)
    return render(request, 'base/post_form.html', context)


@login_required(login_url='login')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.user != post.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid:
            form.save()
            return redirect('hive')

    context = {'form': form}
    return render(request, 'base/post_form.html', context)


@login_required(login_url='login')
def delete(request, pk):
    post = Post.objects.get(id=pk)

    if request.user != post.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        post.delete()
        return redirect('hive')

    context = {'obj': post}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        message.delete()
        return redirect('hive')

    context = {'obj': message}
    return render(request, 'base/delete.html', context)
