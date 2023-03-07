from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app(request):
    return HttpResponse('<marquee><h1>First app</h1></marquee>')

def second_app(request):
    return HttpResponse('<marquee><h1>second app</h1></marquee>')




