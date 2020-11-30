from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):
   CATEGORIES =(
       ('isAC', 'AC'),
       ('notAC', 'NON-AC'),
       ('delux', 'DELUX'),
       ('single', 'SINGLE'),
       ('double', 'DOUBLE'),
   ) 
   number = models.IntegerField()
   category = models.CharField(max_length =10, choices = CATEGORIES)
   beds = models.IntegerField()
   capacity = models.IntegerField()

   def __str__(self):
       return f'Room Number {self.number} category,{self.category}, with {self.beds} beds for {self.capacity} people.'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    def __str__(self):
        return f'{self.user} booked a {self.room.category} room from {self.check_in} to {self.check_out}.'
