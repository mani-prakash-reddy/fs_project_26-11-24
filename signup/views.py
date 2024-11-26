from django.shortcuts import render
# import cx_Oracle

fn = ""
ln = ""
em = ""
pwd = ""
cpwd = ""

from django.shortcuts import render
from login.models import User

def signaction(request):
    if request.method == "POST":
        try:
            # Create new user using ORM
            User.objects.create(
                firstname=request.POST.get("rfname"),
                lastname=request.POST.get("rlname"), 
                email=request.POST.get("remail"),
                password=request.POST.get("rpsw")
            )
            return render(request, "signup_page.html", {
                "openregister": True,
                "success": "Registration successful!"
            })
        except Exception as e:
            return render(request, "signup_page.html", {
                "openregister": True,
                "error": "Registration failed. Please try again."
            })
            
    return render(request, "signup_page.html", {"openregister": True})