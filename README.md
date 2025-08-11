# TN Bus Reservation System 🚌

A Django-based **Bus Reservation System** for Tamil Nadu bus routes, featuring search, booking, cancellation, and refund functionalities.

## 🚀 Features
- **Search for Available Routes** – Filter buses by origin, destination, and date.  
- **Return Trip Option** – Book round trips in a single search.  
- **Seat Availability & Fare Details** – View remaining seats and ticket cost.  
- **Cancellation & Refund** – Cancel tickets up to 2 hours before departure with refund processing.  
- **Attractive UI** – Designed with HTML, CSS, and Bootstrap for a user-friendly interface.  
- **Tamil Nadu Bus Routes Data** – Preloaded with real TN bus route timings and fares.  

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default) / can be upgraded to PostgreSQL
- **Version Control:** Git & GitHub

## 📂 Project Structure
bus_reservation/
│── templates/ # HTML templates
│── static/ # CSS, JS, images
│── routes/ # Route data and logic
│── bookings/ # Booking & cancellation logic
│── manage.py
│── db.sqlite3

## 💻 Installation
```bash
# Clone the repository
git clone https://github.com/LekhasriS/TN-bus-reservation.git

# Navigate into the project
cd TN-bus-reservation

# Install dependencies
pip install -r requirements.txt

# Run the development server
python manage.py runserver

