from django.db import models

class Route(models.Model):
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    departure_time = models.TimeField()
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    travel_date = models.DateField()

    def __str__(self):
        return f"{self.from_location} ➜ {self.to_location} on {self.travel_date}"

class Booking(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    seat_number = models.IntegerField()
    payment_completed = models.BooleanField(default=False)  # 👈 Add this line

    def __str__(self):
        return f"{self.passenger_name} - Seat {self.seat_number} on {self.route}"

    