from django.shortcuts import render

# Create your views here.
def discussHome(request):
    return render(request,'discussionForums/discussHome.html')