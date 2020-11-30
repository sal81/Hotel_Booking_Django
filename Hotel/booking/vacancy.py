import datetime
from Hotel.models import Room,Booking

def check_vacancy(room,check_in, check_out):
    vacancy_list = []
    booking_list = Booking.objects.filter(room= room)
    for booking in booking_list:
        if booking.check_in>check_out or booking.check_out<check_in:
            vacancy_list.append(True)
        else:
            vacancy_list.append(False)
    return all(vacancy_list)
