#function based views


# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Home Page")

# def about(request):
#     return HttpResponse("About Page")

# def contact(request):
#     return HttpResponse("Contact Page")


#class based views

from django.views import View
from django.http import HttpResponse


class Home(View):

    def get(self, request):
        return HttpResponse("Home Page")


class About(View):

    def get(self, request):
        return HttpResponse("About Page")


class Contact(View):

    def get(self, request):
        return HttpResponse("Contact Page")