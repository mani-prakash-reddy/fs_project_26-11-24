from django.shortcuts import render

# Create your views here.

# import cx_Oracle
em = ""
pwd = ""
# Create your views here.
from django.shortcuts import render
from login.models import Staff, Flight, StaffLogin, StaffPhone


def staffloginaction(request):
    if request.method == "POST":
        email = request.POST.get("semail")
        password = request.POST.get("spsw")

        try:
            staff_login = StaffLogin.objects.get(email=email, password=password)
            staff = staff_login.staff
            phone = StaffPhone.objects.filter(staff=staff).first().phone
            request.session["name"] = f"{staff.first_name} {staff.last_name}"
            return render(
                request,
                "staff_welcome.html",
                {
                    "sname": request.session["name"],
                    "c": staff,
                    "ph": phone,
                    "email": staff_login.email,
                },
            )

        except StaffLogin.DoesNotExist:
            return render(
                request,
                "login_page.html",
                {"sf": "Invalid credentials", "stafflogin": True},
            )

    return render(request, "staff_page.html")


def addflightaction(request):
    if request.method == "POST":
        flight = Flight.objects.create(
            flight_no=request.POST.get("fno"),
            flight_name=request.POST.get("fname"),
            from_city=request.POST.get("fr"),
            to_city=request.POST.get("to"),
            arrival=request.POST.get("adate").replace("T", " "),
            departure=request.POST.get("ddate").replace("T", " "),
            available_seats=request.POST.get("avseats"),
            price=request.POST.get("price"),
            staff_id=request.POST.get("sno"),
        )
        return render(
            request,
            "newflight.html",
            {
                "sname": request.session["name"],
                "fadd": "Flight details are added successfully",
            },
        )

    return render(request, "newflight.html", {"sname": request.session["name"]})


def manageflightaction(request):
    if request.method == "POST":
        flight_no = request.POST.get("flyno")
        Flight.objects.filter(flight_no=flight_no).update(deleted=True)

    # Get all non-deleted flights and convert to values
    flights = Flight.objects.filter(deleted=False).values_list(
        'flight_no',
        'flight_name', 
        'from_city',
        'to_city',
        'arrival',
        'departure',
        'available_seats',
        'price'
    )
    
    return render(
        request,
        "manageflights.html",
        {"sname": request.session["name"], "ser": flights},
    )
