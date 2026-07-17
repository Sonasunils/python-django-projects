

from django.shortcuts import render

def result(request):

    students = [
        {"name":"Arun","mark":90},
        {"name":"Anu","mark":40},
        {"name":"Rahul","mark":75},
        {"name":"Diya","mark":25},
    ]

    return render(request,"result.html",{"students":students})