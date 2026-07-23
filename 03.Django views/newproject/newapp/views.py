#function based views


from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("new app Home Page")

def about(request):
    return HttpResponse("new app About Page")

def contact(request):
    return HttpResponse("new app Contact Page")