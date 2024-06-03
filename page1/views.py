from django.shortcuts import render

def home(request):
    return render(request,'home.html',{})

def innerpage(request):
    return render(request,'innerpage.html',{})
