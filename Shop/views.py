from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return render(request,'Shop/index.html')

def about(request):
    return HttpResponse("We are at About")

def contact(request):
    return HttpResponse("We are at Contact")

def tracker(request):
    return HttpResponse("We are at Tracker")

def productView(request):
    return HttpResponse("We are at ProductView")

def search(request):
    return HttpResponse("We are at Search")

def checkout(request):
    return HttpResponse("We are at Checkout")
