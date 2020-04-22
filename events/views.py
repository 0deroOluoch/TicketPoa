import json

from django.core.mail import EmailMessage
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from xhtml2pdf import pisa
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from . models import Event,Ticket,Transaction,Order
from mpesa.transaction import mpesa_push




class EventListView(ListView):
    model = Event
    template_name = 'events/home.html'
    context_object_name = 'events'
    ordering = ['-date_posted']
    paginate_by = 8


def event_details(request,slug):
    event = Event.objects.get(slug=slug)
    tickets = Ticket.objects.filter(event=event)
    return render(request,"events/event_detail.html",{'event':event,'tickets':tickets})

@csrf_exempt
def purchase_event(request):
    if request.is_ajax():
        data = json.loads(request.body.decode('utf-8'))
        name = data['name']
        email = data['email']
        phone = '254' + data['phone'][-9:]
        total = data['total']
        tickets = data['tickets']
        trans = Transaction.objects.create(amount=total,phone=phone)
        for key in tickets.keys():
            for x in range(int(tickets[key])):
                ticket = Ticket.objects.get(id=key)
                order = Order.objects.create(transaction=trans,name=name,email=email,phone=phone,ticket=ticket)
        t = mpesa_push(PhoneNumber=phone,name=name,desc='ticketpoa',id=trans.id)
    return JsonResponse({'data':True})

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa


class Render:
    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return response.getvalue()
        else:
            return "Error Rendering PDF"

def send_tickets(orders):
    email = EmailMessage(subject='Ticket',body="You have succesfully purchased tickets",from_email='admin@ticketpoa.com',to=[orders[0].email])
    for order in orders:
        ticket_file = Render.render('events/ticket.html', {'order': order})
        file_name = '{}-ticket.pdf'.format(order.ticket.name)
        email.attach(file_name,ticket_file,'application/pdf')
    email.send()
    return True


    
class EventCreateView(LoginRequiredMixin,CreateView):
    model = Event
    fields = ['Event_name','Event_descroption','start_date','end_date','Mobile_Money_payment','Visa_cared_payment','Payment_in_installment','Private_event','Free_Event']

    def form_valid(self,form):
         form.instance.shop = self.request.user
         return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Event
    fields = ['Event_name','Event_descroption','start_date','end_date','Mobile_Money_payment','Visa_cared_payment','Payment_in_installment','Private_event','Free_Event']


    def form_valid(self,form):
         form.instance.shop = self.request.user
         return super().form_valid(form)

    def test_func(self):
         event = self.get_object()
         if self.request.user == event.shop:
             return True
         return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/events'

    def test_func(self):
         event = self.get_object()
         if self.request.user == event.shop:
             return True
         return False






class EventOrderCreateView(CreateView):
    model = Event
    fields = ['Client_name','event_ordered']

  





