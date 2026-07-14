from django.http import HttpResponse
def hello(request):
    return HttpResponse("hello")

def new(request):
    return HttpResponse("new")