from django import forms
from apps.hotel_admin.models import AdminUser
from apps.hotels.models import Hotel
from apps.rooms.models import Room
from utils.ConfigLoader import ConfigLoader
from utils.SharedServices import common_attrs


class RoomForm(forms.Form) :
    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop('id', None)  # 👈 ALWAYS SET
        super().__init__(*args, **kwargs)

        hotels = Hotel.objects.values("hotel_id", "name", "city")

        self.fields['hotel'].choices = [
            (item["hotel_id"], f"{item['name']} ({item['city']})")
            for item in hotels
        ]

        value = ConfigLoader.load_config()
        self.fields['room_type'].choices = [
            (item["room_type"], item["description"] + ' ('+ str(item["min_capacity"]) +'-'+ str(item["max_capacity"])+')') for item in value
        ]

    room_number = forms.CharField(label='Room Number', max_length=50, widget=forms.TextInput(attrs=common_attrs('room_number','Enter your room_number')))
    room_type = forms.ChoiceField(label='Room Type',
                               initial='male',
                               choices=[],
                               widget=forms.Select(attrs=common_attrs('room_type', 'Select your room_type'))
                            )
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs=common_attrs('description', 'Enter your description')))
    price_per_night = forms.CharField(label='Price Per Night', widget=forms.TextInput(attrs=common_attrs('price_per_night', 'Enter your price_per_night', 'number notwhitespace', '6')))
    capacity = forms.CharField(label='Capacity', widget=forms.TextInput(attrs=common_attrs('capacity', 'Enter your capacity', 'number notwhitespace', '1')))
    max_capacity = forms.CharField(label='Max Capacity', widget=forms.TextInput(
        attrs=common_attrs('max_capacity', 'Enter your max_capacity', 'number notwhitespace', '2')))
    floor = forms.CharField(label='Floor Number', widget=forms.TextInput(
        attrs=common_attrs('floor', 'Enter your floor', 'number notwhitespace', '2')))
    hotel = forms.ChoiceField(label='Hotel Name',
                                  initial='male',
                                  choices=[],
                                  widget=forms.Select(attrs=common_attrs('hotel', 'Select your hotel', 'select2'))
                                  )


    def clean(self):
        cleaned_data = super().clean()
        room_number = self.cleaned_data.get('room_number')
        capacity = self.cleaned_data.get('capacity')
        max_capacity = self.cleaned_data.get('max_capacity')
        hotel = cleaned_data.get('hotel')
        if room_number == '':
            self.add_error('room_number', 'Please enter a room number')
        if room_number is not None and hotel:
            existRoomNumber = Room.objects.filter(room_number=room_number, hotel_id=hotel)
            if existRoomNumber:
                self.add_error('room_number', 'This room number is already in use')

        if capacity == '':
            self.add_error('capacity', 'Please enter at capacity')
        if max_capacity == '':
            self.add_error('max_capacity', 'Please enter at max capacity')
        if int(max_capacity) < int(capacity):
            self.add_error('max_capacity', 'Please enter more capacity')

        return cleaned_data