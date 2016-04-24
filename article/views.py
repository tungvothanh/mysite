from django.shortcuts import render
from django.http import HttpResponse
from article.models import Posts
import pymongo

def index(request):

    client = pymongo.MongoClient("mongodb://vothanhtung:123456@ds013848.mlab.com:13848/blog")

    db = client.blog

    # print db.collection_names()
    print("did you com herere??????????????")
    return HttpResponse("Hello, world. You're at the polls index.")

def top(request):

    client = pymongo.MongoClient("mongodb://vothanhtung:123456@ds013848.mlab.com:13848/blog")

    db = client.blog

    # print db.collection_names()
    print("did you com herere??????????????")

    return render(request, 'top/top.html')

def add(request):
    print("ok")

    post = Posts()
    # tot nhaat le nen co function upload word len
    # sau day co othe la tao mot cai hung html voi cac the nhu vay
    # oki, khong qua kho chi la lam de hoc thoi ma
    # khong co gi qua ghe gom ca
    # sau 1 nam it nhat phai co cai gi de show chuw?
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        post.title = title
        post.content =content
        post.save()
        print(post)

    return render(request,'article/add.html')

def list(request):

    lists = Posts.objects.all()

    # print(lists)

    return render(request,'article/list.html',{'lists':lists})

def test_mongo():
    #
    client = pymongo.MongoClient("mongodb://<vothanhtung>:<Tungvt91@>@ds017231.mlab.com:17231/blog")

    db = client.blog

