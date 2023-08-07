from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# reverse takes input name of a url addition
# and figures out the whole url on its own

from .models import Flight, Passenger


# Create your views here.
def index(request):
    saves = Flight.objects.prefetch_related('origins').all()
    p = [save.origins for save in saves]
    return render(request, "flights/index.html",{
        "flights": p
    })


def flight(request, flight_id):
    # get me the flight matching the flight id in url
    # aik flight la ke do
    flight = Flight.objects.get(id=flight_id)
    # 3also
    # flight = Flight.objects.get(pk=flight_id)
    # uss aik flight pe jonse passnegers phle se book
    passengers = flight.passengers.all()
    all_passengers = Passenger.objects.all()
    # print(passengers)
    non_passengers = all_passengers.difference(passengers)
    return render(request, "flights/flights.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })

# * idhr form aik template pe hai lekin post pe 
# wo dosra VIEW execute kr rha hai
# { kyun k form aisa hai k glt input nhi askti}
# view ko alehda krne ki zrort isliye bhi hai
# le iss view ko slect from ke zariya 
# non_passenger(jisko flight per ab post ke zariye boook krna)
# uski passenger.id bhi chahiye
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
                                        # kyun k select form
                                        # se aa passenger id rhi hai
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight) # multiple flights book kr skte
                                            # flight hai
        return HttpResponseRedirect(reverse("flights", args=({flight.id})))
                                                    # ye view 
                                                    # ka
                                                    #argument
                                                    # in form
                                                    # of tuple i.e multiple 
                                                    # ho skti