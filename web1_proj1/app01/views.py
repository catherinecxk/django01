from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def home(requests):
    return HttpResponse("<h1>hello world</h1>")