from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Room, Booking
from .forms import AvailabilityForms
from Hotel.booking.vacancy import check_vacancy

# Create your views here.

class RoomList(ListView):
    model = Room

class BookingList(ListView):
    model = Booking

class BookingView(FormView):
    form_class = AvailabilityForms
    template_name = "vacancy_form.html"

    def form_valid(self,form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category = data['room_category'])
        vacant_rooms =[]
        for room in room_list:
            if check_vacancy(room, data['check_in'], data['check_out']):
                vacant_rooms.append(room)
        
        if(len(vacant_rooms)):
            room = vacant_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out'],

            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse("No booking available for this category.")






