# gameshow/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("<str:room_name>/user/", views.user, name="user"),
    path("<str:room_name>/host", views.host, name="host"),
]