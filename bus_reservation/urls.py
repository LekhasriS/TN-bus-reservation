from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('busbooking.urls')),  # Make sure this matches your app name exactly
]
