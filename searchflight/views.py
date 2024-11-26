from django.shortcuts import render

# from searchflight.models import flightsearch
# Create your views here.
"""def searchflightaction(request):
    search=flightsearch.objects.all()
    print("output",search)
    return render(request,'searchflight.html',{'ser':search})"""


from django.shortcuts import render
from login.models import Passenger, Flight, StaffLogin


# import cx_Oracle
def searchflightaction(request):
    flights = Flight.objects.filter(deleted=False)
    return render(request, "searchflight.html", {"ser": flights})
