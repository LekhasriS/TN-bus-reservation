from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import Route, Booking
from django.views.decorators.csrf import csrf_exempt

# Home page
def home(request):
    return render(request, 'home.html')

# Search bus routes
def search_routes(request):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        date = request.POST.get('date')

        routes = Route.objects.filter(
            from_location__iexact=source,
            to_location__iexact=destination,
            travel_date=date
        )

        return render(request, 'search_results.html', {
            'routes': routes,
            'source': source,
            'destination': destination,
            'date': date
        })
    return redirect('home')

# Book a ticket
def book_ticket(request, route_id):
    route = get_object_or_404(Route, id=route_id)

    booked_seats = Booking.objects.filter(
        route=route,
        payment_completed=True
    ).values_list('seat_number', flat=True)

    if request.method == 'POST':
        name = request.POST.get('passenger_name')
        seat_number = request.POST.get('seat_number')

        if int(seat_number) in booked_seats:
            return render(request, 'error.html', {'message': 'Seat already booked!'})

        booking = Booking.objects.create(
            route=route,
            passenger_name=name,
            seat_number=seat_number,
            status="Confirmed"
        )
        return redirect('payment', booking_id=booking.id)

    seat_numbers = list(range(1, 41))  # Assume 40 seats

    return render(request, 'book_ticket.html', {
        'route': route,
        'booked_seats': list(booked_seats),
        'seat_numbers': seat_numbers
    })

# Payment page
def payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        booking.payment_completed = True
        booking.save()
        return render(request, 'payment_success.html', {'booking': booking})

    return render(request, 'payment.html', {'booking': booking})

# Show user bookings with cancel option
def my_bookings(request):
    bookings = Booking.objects.filter(payment_completed=True).select_related('route')
    return render(request, 'my_bookings.html', {'bookings': bookings})

# Cancel a booking (no restriction)
@csrf_exempt
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        booking.status = "Cancelled"
        booking.save()
        return render(request, 'cancel_success.html', {'booking': booking})

    return redirect('my_bookings')
