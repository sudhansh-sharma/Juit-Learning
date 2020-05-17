from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/homeIndex.html')
def about(request):
    return render(request,'home/homeAbout.html')
def contact(request):
    return render(request,'home/homeContact.html')
def terms(request):
    return render(request,'home/homeTerms.html')