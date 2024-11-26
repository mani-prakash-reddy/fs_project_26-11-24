from django.shortcuts import render
from django.http import HttpResponse
from login.models import Passenger
from weasyprint import HTML
from django.template.loader import render_to_string
 
def ticketaction(request):
    pnr = request.session.get("pnr")
    passenger = Passenger.objects.select_related("flight").get(pnr=pnr)
 
    ticket_data = {
        "pnr": passenger.pnr,
        "name": f"{passenger.firstname} {passenger.lastname}",
        "flight_no": passenger.flight.flight_no,
        "from_city": passenger.flight.from_city,
        "to_city": passenger.flight.to_city,
        "arrival": passenger.flight.arrival,
        "seat_no": passenger.seat_no if passenger.seat_no else "NA",
    }
 
    if request.GET.get("format") == "pdf":
        html_string = render_to_string('ticket_pdf.html', {'t': ticket_data})
        html = HTML(string=html_string)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="ticket.pdf"'
        html.write_pdf(response)
        return response
 
    return render(request, "ticket.html", {"t": ticket_data})