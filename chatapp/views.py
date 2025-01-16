from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Hello World: Home Page')
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('Hello World: About Page')
