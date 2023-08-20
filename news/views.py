from django.shortcuts import render

def index(request):
    return render(request,'dashboard.html')

def allnews(request):
    return render(request,'allnews.html')

def allcategory(request):
    return render(request,'allcategory.html')