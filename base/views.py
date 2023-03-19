from django.shortcuts import render

# Create your views here.

posts = [
    {'id': 1, 'username': 'hadisoufan', 'caption': 'Hello Classmates'},
    {'id': 2, 'username': 'cleopatra',
        'caption': 'Just started a new chapter in my book'},
    {'id': 3, 'username': 'melia', 'caption': 'Check out my recent certificate'},
    {'id': 4, 'username': 'zayn', 'caption': 'happy b-day hadi'},
]


def home(request):

    context = {'posts': posts}
    return render(request, 'base/home.html', context)


def post(request, pk):
    post = None
    for i in posts:
        if i['id'] == int(pk):
            post = i
    context = {'post': post}
    return render(request, 'base/post.html', context)
