# busbooking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_routes, name='search_routes'),
    path('book/<int:route_id>/', views.book_ticket, name='book_ticket'),
    path('payment/<int:booking_id>/', views.payment, name='payment'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
