from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from events.models import Event,Ticket
# Create your views here.
@login_required
def merchant(request):
	return render(request,'dashboard/merchant.html',{})

def merchant_account(request):
	return render(request,'dashboard/merchant_account.html',{})

def merchantfinance(request):
	return render(request,'dashboard/merchantfinance.html',{})

def merchantproducts(request):
	return render(request,'dashboard/merchantproducts.html',{})

def merchantprofile(request):
	return render(request,'dashboard/merchantprofile.html',{})

def merchantstores(request):
	return render(request,'dashboard/merchantstores.html',{})

def merchantusers(request):
	return render(request,'dashboard/merchantusers.html',{})

def newstore(request):
	context = {}
	if request.method == "POST":
		store_name = request.POST['store_name']
		desc = request.POST['description']
		date = request.POST['date']
		time = request.POST['time']
		poster = request.FILES['poster']
		location = request.POST['location']
		event = Event(shop=request.user,Event_name=store_name,Event_description=desc,date=date,time=time,Event_poster=poster,location=location)
		event.save()
		tickets = request.POST.getlist('ticket')
		for ticket in tickets:
			data = ticket.split(',')
			Ticket.objects.create(event=event,name=data[0],quantity=data[1],price=data[2])
		context = {'success':True}
	return render(request,'dashboard/newstore.html',context)

def orders(request):
	return render(request,'dashboard/orders.html',{})
