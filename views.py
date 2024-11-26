from django.shortcuts import render, redirect

from login.models import Flight

def bookingaction(request):
    if not request.session.get("islogged", False):
        return render(
            request, "login_page.html", {"bkmsg": "Please login to book the flight"}
        )

    if request.method == "POST":
        from_city = request.POST.get("flyfrom")
        to_city = request.POST.get("flyto")
        arr_date = request.POST.get("date1")

        flights = Flight.objects.filter(
            from_city=from_city, to_city=to_city, arrival__date=arr_date, deleted=False
        )
        flight_details = [
            (
                flight.flight_no,
                flight.flight_name,
                flight.from_city,
                flight.to_city,
                flight.arrival,
                flight.departure,
                flight.available_seats,
                flight.price,
            )
            for flight in flights
        ]
        print("flyhigh", flight_details)

        return render(request, "dum.html", {"se": flight_details})
    return render(request, "booking.html")

def extractno(request):
    if request.method == "POST":
        flightid = request.POST.get("flightid")
        print(flightid)
        # Process the flightid as needed
        return redirect('passenger.html')  # Redirect to the passenger page
    return redirect('booking.html')  # Redirect to the booking page if not a POST request