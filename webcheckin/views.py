from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from login.models import Passenger
# import cx_Oracle
# Create your views here.

wpnr = ""
wfn = ""
wln = ""
l = ""


def webcheckinaction(request):
    if not request.session.get("islogged", False):
        return render(
            request, "login_page.html", {"bkmsg": "Please Login to webcheck in"}
        )

    if request.method == "POST":
        pnr = request.POST.get("pnrno")
        firstname = request.POST.get("pnrfn")
        lastname = request.POST.get("pnrln")

        try:
            passenger = Passenger.objects.get(
                pnr=pnr, firstname=firstname, lastname=lastname
            )
            return render(request, "web_check.html")
        except Passenger.DoesNotExist:
            return render(request, "web_check.html", {"webmsg": "Invalid credentials"})

    return render(request, "web_check.html")


from django.shortcuts import render
from login.models import Passenger


def checkindetailsaction(request):
    if request.method == "POST":
        pnr = request.POST.get("pnrno")
        firstname = request.POST.get("pnrfn")
        lastname = request.POST.get("pnrln")

        try:
            passenger = Passenger.objects.select_related('flight').get(
                pnr=pnr, firstname=firstname, lastname=lastname
            )

            if passenger.seat_no:
                return render(
                    request,
                    "web_check.html",
                    {"webmsg": "Your web checkin has already processed"},
                )

            flight = passenger.flight
            available_seats = list(range(1, flight.available_seats + 1))
            taken_seats = (
                Passenger.objects.filter(flight=flight)
                .exclude(seat_no__isnull=True)
                .values_list("seat_no", flat=True)
            )
 
            available_seats = [s for s in available_seats if s not in taken_seats]
            print("seatsloading", passenger)
            print("Available seats:", available_seats)

            return render(
                request,
                "checkindetails.html",
                {"flypnr": passenger, "seatno": available_seats, "flight": flight},
            )

        except Passenger.DoesNotExist:
            return render(request, "web_check.html", {"webmsg": "Invalid credentials"})

    return render(request, "checkindetails.html")


def seatcheckin(request):
    if request.method == "POST":
        pnr = request.POST.get("sepnr")
        seat_no = request.POST.get("seat")

        try:
            passenger = Passenger.objects.select_related('flight').get(pnr=pnr)
            
            # Check if passenger is already checked in
            if passenger.checkin_status:
                return render(request, "web_check.html", 
                    {"webmsg": "Passenger already checked in"})

            flight = passenger.flight
            
            # Verify seat is still available
            if flight.available_seats <= 0:
                return render(request, "web_check.html", 
                    {"webmsg": "No seats available"})

            # Update passenger details
            passenger.seat_no = seat_no
            passenger.checkin_status = True
            passenger.save()

            # Update flight's available seats
            flight.available_seats = flight.available_seats - 1
            flight.save()

            passenger_details = Passenger.objects.select_related("flight").get(pnr=pnr)
            return render(request, "tic_seat.html", {"t": passenger_details})

        except Passenger.DoesNotExist:
            return render(request, "web_check.html", 
                {"webmsg": "Invalid PNR"})

    elif request.method == "GET" and request.GET.get("format") == "pdf":
        try:
            pnr = request.GET.get("pnr")
            if not pnr:
                return HttpResponse('PNR not provided', status=400)
                
            passenger_details = get_object_or_404(Passenger.objects.select_related("flight"), pnr=pnr)
            
            # Configure PDF generation
            template_path = 'final_ticket.html'
            context = {'t': passenger_details}
            
            # Create a Django response object with PDF mime type
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="boarding_pass_{pnr}.pdf"'
            
            # Load and render the template
            template = get_template(template_path)
            html = template.render(context)
            
            # Create PDF
            pisa_status = pisa.CreatePDF(html, dest=response, encoding='UTF-8')
            
            if pisa_status.err:
                return HttpResponse('PDF generation failed')
                
            return response
            
        except Exception as e:
            print(f"PDF generation error: {str(e)}")
            return HttpResponse('PDF generation failed', status=500)

    return render(request, "tic_seat.html")


def stafffwebcheckin(request):
    # if not request.session.get('islogged', False):
    # return render(request,'login_page.html',{'bkmsg':'Please Login to webcheck in'})
    global wpnr, wfn, wln, l
    if request.method == "POST":
        connStr = "system/password@localhost:1521/xe"
        m = cx_Oracle.connect(connStr)
        cursor = m.cursor()
        d = request.POST
        # m.close()
        for key, value in d.items():
            if key == "pnrno":
                wpnr = value
            if key == "pnrfn":
                wfn = value
            if key == "pnrln":
                wln = value
        c = "SELECT * FROM Passenger WHERE PNR='{}' and Fname='{}' and Lname='{}'".format(
            wpnr, wfn, wln
        )
        cursor.execute(c)

        # m.commit()
        print(c)
        # t=list(cursor.fetchall())
        if not c:
            return render(request, "web_check.html", {"webmsg": "Invalid credentials"})
        # print(t)

    return render(request, "staffwebcheckin.html")
