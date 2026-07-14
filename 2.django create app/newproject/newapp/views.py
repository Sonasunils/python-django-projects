from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello welcome")
def index2(request):
    return HttpResponse("hello welcome2")

