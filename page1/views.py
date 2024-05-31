from django.shortcuts import render


def home(request):
    return render(request,'page1/home.html')

def about(request):
    return render(request,'page1/about.html',{'title':'about'})

def Branch(request):
    return render(request,'page1/Branch.html',{'title':'Branch'})

def YearWise(request):
    return render(request,'page1/YearWise.html',{'title':'YearWise'})

def Roundwise(request):
    return render(request,'page1/Roundwise.html',{'title':'Roundwise'})