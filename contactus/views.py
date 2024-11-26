# contactus/views.py
from django.shortcuts import render
from login.models import Passenger, Flight, StaffLogin  # Import from login app
from .models import ContactUs  # Import only ContactUs from local models

def contactusaction(request):
    if request.method == "POST":
        ContactUs.objects.create(
            email=request.POST.get("conem"),
            name=request.POST.get("conname"), 
            country=request.POST.get("concountry"),
            phone=request.POST.get("conphno")
        )
    return render(request, "contactus.html")

def passqueries(request):
    queries = ContactUs.objects.all()
    return render(request, "pass_queries.html", {
        "qu": queries,
        "sname": request.session["name"]
    })