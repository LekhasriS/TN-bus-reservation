from django.core.management.base import BaseCommand
from busbooking.models import Route
from datetime import date, timedelta, time
import random

class Command(BaseCommand):
    help = "Generate Tamil Nadu bus routes for the next 5 years"

    def handle(self, *args, **kwargs):
        # Major Tamil Nadu cities
        cities = [
            "Chennai", "Coimbatore", "Madurai", "Trichy", "Salem",
            "Tirunelveli", "Erode", "Thanjavur", "Vellore", "Tiruvannamalai",
            "Dindigul", "Karur", "Nagercoil", "Kanchipuram", "Thoothukudi"
        ]

        # Generate route pairs (not same city)
        routes_data = []
        for i in range(len(cities)):
            for j in range(len(cities)):
                if i != j:
                    # Random departure time (6 AM to 11 PM)
                    hour = random.choice(range(6, 23))
                    minute = random.choice([0, 30])
                    departure_time = time(hour, minute)

                    # Random fare (₹200 – ₹800 depending on distance)
                    fare = random.choice([200, 250, 300, 350, 400, 450, 500, 600, 700, 800])

                    routes_data.append((cities[i], cities[j], departure_time, fare))

        start_date = date.today()
        end_date = start_date + timedelta(days=365 * 5)  # 5 years

        created_count = 0
        skipped_count = 0

        current_date = start_date
        while current_date <= end_date:
            for from_loc, to_loc, departure_time, fare in routes_data:
                route, created = Route.objects.get_or_create(
                    from_location=from_loc,
                    to_location=to_loc,
                    travel_date=current_date,
                    departure_time=departure_time,
                    fare=fare
                )
                if created:
                    created_count += 1
                else:
                    skipped_count += 1
            current_date += timedelta(days=1)

        self.stdout.write(self.style.SUCCESS(
            f"✅ Routes generated for {len(cities)} cities, {created_count} new, {skipped_count} skipped."
        ))
