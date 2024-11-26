from django.shortcuts import render

# import cx_Oracle
import datetime
# Create your views here.
# def bookingaction(request):
# return render(request,'booking.html')

# def searchflightaction(request):
# return render(request,'searchflight.html')


fr = ""
to = ""
l = []
arr_date = ""
# dep_date=''
# Create your views here.
from django.shortcuts import render
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
            {
                "flight_no": flight.flight_no,
                "flight_name": flight.flight_name,
                "from_city": flight.from_city,
                "to_city": flight.to_city,
                "arrival": flight.arrival,
                "departure": flight.departure,
                "available_seats": flight.available_seats,
                "price": flight.price,
            }
            for flight in flights
        ]
        print("flyhigh", flight_details)

        return render(request, "dum.html", {"se": flight_details})
    return render(request, "booking.html")


def dumaction(request):
    return render(request, "dum.html", {"se": l})


def webcheckinaction(request):
    return render(request, "webcheckin.html")


def extractflytno(request):
    if request.method == "POST":
        flight_id = request.POST.get("flightid")
        return render(request, "passenger.html", {"flightid": flight_id})
    return render(request, "dum.html")