from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome to My Vlog Channel</h1>")


def vlog(request, vlog_id):
    return HttpResponse(f"""
    <h2>Vlog #{vlog_id}</h2>
    <p>Thanks for watching Vlog Number {vlog_id}.</p>
    """)


def category(request, category_name):
    return HttpResponse(f"""
    <h2>{category_name.title()} Vlogs</h2>
    <p>Showing all {category_name} related videos.</p>
    """)


def vlog_details(request, category_name, vlog_id):
    return HttpResponse(f"""
    <h2>{category_name.title()} Vlog</h2>
    <h3>Video Number: {vlog_id}</h3>
    """)