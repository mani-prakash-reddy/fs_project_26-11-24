
from django.shortcuts import render
from django.template.loader import get_template

def ticket_view(request):
    # ...existing code...
    if request.GET.get('format') == 'pdf':
        template = get_template('pdf_ticket.html')
        # ...rest of PDF generation code...
    else:
        template = get_template('ticket.html')
    # ...existing code...