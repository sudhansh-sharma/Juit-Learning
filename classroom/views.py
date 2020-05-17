from django.shortcuts import render

# Create your views here.
def classHome(request):
    return render(request,'classroom/classHome.html')