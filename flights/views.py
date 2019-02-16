from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "flights": Flight.objects.all()
    }

    return render(request, "flights/index.html", context=context)


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight Does not exist")

    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    }

    return render(request, "flights/flight.html", context=context)


def book(request, flight_id):
    
    passenger_id = int(request.POST['passenger'])
    passenger = Passenger.objects.get(pk=passenger_id)
    flight = Flight.objects.get(pk=flight_id)

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))


def cancel(request, flight_id, passenger_id):
    
    passenger = Passenger.objects.get(pk=passenger_id)
    flight = Flight.objects.get(pk=flight_id)



    passenger.flights.remove(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
