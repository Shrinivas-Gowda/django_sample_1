from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app2(request):
    return HttpResponse('<marquee><h1>First app2</h1></marquee>')

def second_app2(request):
    return HttpResponse('<marquee><h1>Second app2</h1></marquee>')