from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Pavan(request):
    return HttpResponse('<marquee><h1>work smart not hard</h1></marquee>')

def kalayan(request):
    return HttpResponse('<marquee><h1>EVERY PERSON WILL GET A CHANCE</h1></marquee>') 

