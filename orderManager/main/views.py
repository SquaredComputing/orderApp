from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>test</h1>")

def orders(response):
    return HttpResponse("this will be the order page")
