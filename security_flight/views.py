from django.shortcuts import render

from login.models import Passenger, Flight, SecurityOfficer


# import cx_Oracle
# Create your views here.
def securitystarusaction(request):
    if request.method == "POST":
        pnr = request.POST.get("sepnr")

        passenger = Passenger.objects.get(pnr=pnr)
        passenger.security_status = True
        passenger.save()

        return render(
            request,
            "security.html",
            {
                "msg": f"PNR NO: {pnr} has completed security checkup",
                "secname": request.session["secname"],
            },
        )

    return render(
        request, "security.html", {"msg": "", "secname": request.session["secname"]}
    )


secem = ""
secpwd = ""


# Create your views here.
def securityloginaction(request):
    if request.method == "POST":
        email = request.POST.get("secemail")
        password = request.POST.get("secpsw")
        
        try:
            officer = SecurityOfficer.objects.get(email=email, password=password)
            request.session["secname"] = f"{officer.first_name} {officer.last_name}"
            
            # Pass individual fields instead of the whole object
            return render(request, "security_welcome.html", {
                "sname": request.session["secname"],
                "officer_id": officer.sec_id,
                "area": officer.area,
                "pin": officer.pin,
                "gate": officer.gate_no,
                "email": officer.email,
                "ph": officer.securityofficerphone_set.first().phone if officer.securityofficerphone_set.exists() else None
            })
            
        except SecurityOfficer.DoesNotExist:
            return render(request, "login_page.html", {
                "secf": "Invalid credentials"})