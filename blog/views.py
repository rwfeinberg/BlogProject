from django.shortcuts import render

posts = [
    {
        'author': 'RyanF',
        'title': 'Post 1',
        'content': 'This is my first post.',
        'date_posted': 'May 27, 2021'
    },
    {
        'author': 'SomeoneElse',
        'title': 'Post 2',
        'content': 'This is my second post.',
        'date_posted': 'May 28, 2021'
    },
    {
        'author': 'ThirdPerson',
        'title': 'Post 3',
        'content': 'This is my 3rd post.',
        'date_posted': 'May 29, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})