from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def home(request):
    posts = Article.objects.all()
    res = '<h1>Список статей</h>'
    for post in posts:
        res += f'<div><h3>{post.title}</h3><div>{post.content}</div></div><hr>'
    return HttpResponse(res)


def test(request):
    return HttpResponse('<h1>Test page!</h1>')