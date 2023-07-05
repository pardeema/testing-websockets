from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name, "user": request.GET.get('username')})

def host(request, room_name):
    return render(request, "host.html", {"room_name": room_name})

def user(request, room_name):
    return render(request, "username.html", {"room_name": room_name})