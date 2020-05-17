from django.urls import path
from discussionForums import views

urlpatterns = [
    path('', views.discussHome, name="discussionHome") ,
]
