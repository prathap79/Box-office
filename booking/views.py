from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from theatre.models import Show
from user_profile.models import UserProfile
from .forms import SeatForm, BookingForm
import datetime

# Create your views here.


def reserve_seat(request, show_id):
	try:
		show_info = Show.objects.get(pk=show_id)
	except Theatre.DoesNotExist:
		raise Http404("Page does not exist")
	form = SeatForm()
	return render(request, 'reserve_seat.html', 
		{'show_info': show_info, 'form': form})


def payment_gateway(request):
	try:
		seats = request.POST.get('selected_seat')
		seat_type = request.POST.get('seat_type')
		show_id = request.POST.get('show_id')

		show = Show.objects.get(pk=show_id)
		seats = seats.split(',')
		book_seat = []
		for each in seats:
			s = Seat.objects.get(no=each, seat_type=seat_type, show=show)
			s.status = "Processing"
			if Seat.objects.filter(no=each, show=show).exists():
				return render(request, 'booking/reserve_seat.html', 
					{'show_info': show, 'form': SeatForm()})

				s.status="Occupied"
				s.save()
				book_seat.append(s)
			else:
				import time
				time.delay(float(180))
				s.staus = "Available"
				s.save()
				return HttpResponseRedirect("/")

	except:
		return HttpResponseRedirect('/home/')



def payment_confirmation(request):
	if request.POST:
		show_id = request.POST.get('show_id')
		show = Show.objects.get(pk=show_id)
		seats = request.POST.get('selected_seat')
		seats = seats.split(',')
		timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		payment_type = request.POST.get('payment_type')
		paid_amount = request.POST.get('amount')
		paid_by = request.user
		id = str(show) + str(seats) + timestamp
		book = Booking(id=id, timestamp=timestamp, payment_type=payment_type, 
			paid_amount=paid_amount, paid_by=paid_by)
		book.save()

		booked_seat = []

		for seat in seats:
			print(seat)
			s = Seat.objects.get(no=seat, show=show)
			b = Booking.objects.get(pk=id)
			booked = BookedSeat(seat=s, booking=b)
			booked_seat.append(booked)

		BookedSeat.objects.bulk_create(booked_seat)

		return render(request, 'booking/payment_confirmation.html')
	else:
		return redirect('theatre.views.theatre_list')
