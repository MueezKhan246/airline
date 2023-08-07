from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    origins = models.ManyToManyField(Airport)
    # departures mean all the flights leaving from that airport i.e, having origin there
    # destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
     #string representation of a python model
    def __str__(self):
        return f"{self.id}: {self.origins}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # conflict of understanding
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
                                            # a passenger can have no flights
                                            # if we flight we can get all its passengers
    def __str__(self):
        return f"{self.first} {self.last}"

class Check(models.Model):
    checks = models.BooleanField(default=True)
