from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def top(request):
    return HttpResponse("Hello, wor????????ld. You're at the polls index.")
