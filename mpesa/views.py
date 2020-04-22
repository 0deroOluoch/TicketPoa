import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from events.models import Transaction
from events.views import send_tickets

@csrf_exempt
def mpesa_callback(request,id):
	data = json.loads(request.body.decode('utf-8'))
	result_code = data['Body']['stkCallback']['ResultCode']
	mpesa_code = data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
	t = Transaction.objects.get(id=id)
	if result_code == 0:
		t.complete = True
		t.mpesa_code = mpesa_code
		t.save()
		send_tickets(t.order_set.all())
	else:
		t.delete()
	return HttpResponse('callback')
