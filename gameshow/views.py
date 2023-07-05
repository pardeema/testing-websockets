from django.shortcuts import render
from random import randint

# Create your views here.
def index(request):
    return render(request, "index.html")

def room(request, room_name):
    if request.GET.get('username') != None:
        user = request.GET.get('username')
    else:
        user = "Guest{}".format(randint(1,1000))
    return render(request, "room.html", {"room_name": room_name, "user": user})

def host(request, room_name):
    return render(request, "host.html", {"room_name": room_name})

def user(request, room_name):
    return render(request, "username.html", {"room_name": room_name})