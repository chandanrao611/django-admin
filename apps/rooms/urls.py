from django.urls import path
from apps.rooms.views import RoomListView, ManageRoomView

app_name = "rooms"
urlpatterns = [
    path('', RoomListView.as_view(), name='room-list'),
    path('/add', ManageRoomView.as_view(), name='add-room'),
]