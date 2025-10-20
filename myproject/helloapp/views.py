from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    """返回Hello World消息的视图函数"""
    return HttpResponse("<h1>Hello World!</h1><p>欢迎来到Django helloapp应用！</p>")

def hello_name(request, name):
    """返回个性化问候消息的视图函数"""
    return HttpResponse(f"<h1>Hello, {name}!</h1><p>很高兴见到你！</p>")

def singlepage(request):
    """返回单页面应用的视图函数"""
    return render(request, 'helloapp/singlepage.html')

def react_hello(request):
    """返回React Hello组件应用的视图函数"""
    return render(request, 'helloapp/react_hello.html')

def react_counter(request):
    """返回React计数器应用的视图函数"""
    return render(request, 'helloapp/react_counter.html')

def react_addition(request):
    """返回React加法游戏应用的视图函数"""
    return render(request, 'helloapp/react_addition.html')
