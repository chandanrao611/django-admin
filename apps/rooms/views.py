from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from pprint import pprint
from apps.hotel_admin.forms import FileForm
from apps.rooms.forms import RoomForm
from apps.rooms.models import Room
from utils.MessageHandler import MessageHandler


class RoomListView(View):
    def get(self, request):
        rooms = Room.objects.select_related('hotel').all()
        # Create paginator: 10 employees per page
        limit = int(request.GET.get('limit', 10))
        paginator = Paginator(rooms, limit)
        # Get current page number from query string (?page=2)
        page_number = request.GET.get('page', 1)
        # Get the page object
        page_obj = paginator.get_page(page_number)
        fileForm = FileForm()
        request.show_loader = False
        pprint(list(page_obj.object_list.values()))
        return render(request, 'room-list.html', {'page_obj': page_obj, 'fileForm': fileForm})

class ManageRoomView(View):
    def get(self, request):
        request.show_loader = True
        form = RoomForm()
        request.show_loader = False
        return render(request, 'manage-room.html', {'form': form})

    def post(self, request):
        request.show_loader = True
        form = RoomForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            pprint(cd)
            Room.objects.create(
                room_number=cd['room_number'],
                room_type=cd['room_type'],
                price_per_night=cd['price_per_night'],
                capacity=cd['capacity'],
                max_capacity=cd['max_capacity'],
                floor=cd['floor'],
                description=cd['description'],
                hotel_id=cd['hotel']
            )
            MessageHandler.success(request, 'Added successfully.v')
            request.show_loader = False
            return redirect('/rooms')
        request.show_loader = False
        return render(request, 'manage-room.html', {'form': form})
