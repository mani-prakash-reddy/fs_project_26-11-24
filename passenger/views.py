from django.shortcuts import render

# import cx_Oracle
import string
import random  # define the random module
from payment.views import paymentaction

# Create your views here.
# def passengeraction(request):
#   return render(request,'passenger.html')
pfn = ""
pln = ""
gen = ""
nan = ""
flightno = ""
phno = ""
# ran = ''.join(random.choices(string.ascii_uppercase + string.digits,k =6))
# rand=str(ran)
# print("----------------------------------------------------",rand)

from login.models import Passenger, Flight, StaffLogin
from django.utils.crypto import get_random_string
from login.models import Passenger, PassengerPhone
from django.db import transaction


# Create your views here.
def passengeraction(request):
    if request.method == "POST":
        try:
            with transaction.atomic():
                # Generate PNR
                pnr = get_random_string(
                    6, allowed_chars=string.ascii_uppercase + string.digits
                )
                request.session["pnr"] = pnr

                # Create passenger without phone
                passenger = Passenger.objects.create(
                    pnr=pnr,
                    firstname=request.POST.get("pfname"),
                    lastname=request.POST.get("plname"),
                    gender=request.POST.get("pgender"),
                    nationality=request.POST.get("pnan"),
                    flight_id=request.POST.get("flightid"),
                    security_status=False,
                    checkin_status=False,
                )
                print(f"Passenger created: PNR={passenger.pnr}, Firstname={passenger.firstname}, "
      f"Lastname={passenger.lastname}, Gender={passenger.gender}, "
      f"Nationality={passenger.nationality}, Flight ID={passenger.flight_id}, "
      f"Security Status={passenger.security_status}, Check-in Status={passenger.checkin_status}")
                # Create passenger phone record
                if phone := request.POST.get("phno"):
                    PassengerPhone.objects.create(passenger=passenger, phone=phone)

                return render(request, "payment.html")

        except Exception as e:
            return render(
                request, "passenger.html", {"error": "Error creating passenger record"}
            )

    return render(request, "passenger.html")