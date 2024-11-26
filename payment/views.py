from django.shortcuts import render

# import cx_Oracle
import string
import random  # define the random module
import time
# Create your views here.
# def paymentaction(request):
#   return render(request,'payment.html')


cno = ""
cname = ""
exp = ""
cvv = ""
# payment/views.py
from django.shortcuts import render
from django.utils.crypto import get_random_string
from .models import WebvisitorCard
from datetime import datetime

def paymentaction(request):
    if request.method == "POST":
        try:
            # Generate unique card ID
            card_id = "ck" + get_random_string(4, allowed_chars='0123456789')
            
            # Create card record using Django ORM
            WebvisitorCard.objects.create(
                card_id=card_id,
                card_number=request.POST.get("ccnum"),
                card_name=request.POST.get("cardname"),
                cvv=request.POST.get("cardcvv"),
                expiry=datetime.strptime(request.POST.get("cardexp"), "%Y-%m")
            )
            print(f"WebvisitorCard created: Card ID={card_id}, "
      f"Card Number={request.POST.get("ccnum")}, Card Name={request.POST.get("cardname")}, "
      f"CVV={request.POST.get("cardcvv")}")
            print(Expiry=datetime.strptime(request.POST.get("cardexp"), "%Y-%m")
            )

            return render(request, "card.html", {"success": True})
            
        except Exception as e:
            return render(request, "payment.html", {
                "error": "Payment processing failed. Please try again."
            })
            
    return render(request, "payment.html")

def successaction(request):
    time.sleep(4)
    return render(request, "card.html")