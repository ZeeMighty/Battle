from django.http import HttpResponse
from django.template import loader
from . models import event, heroe, date, place
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import View

def IndexView(request):
    events = event.objects.all()
    return render(request, 'mains/homepage.html', {'events': events})

def EventView(request, event_id):
    events = event.objects.filter(id = event_id)
    #event_date = date.objects.get(date_id = event_id)
    event_place = place.objects.filter(place_id = event_id)
    return render(request, 'mains/events.html', {'events': events, 'place': event_place})

def hero(request, heroe_id):
    heroes = get_object_or_404(heroe, pk=heroe_id)
    context = {'heroes': heroes}
    return render(request, 'mains/heroesPage.html', context)

def Dates(request):
    dates = date.objects.all()
    context = {'date': dates}
    return render(request, 'mains/dates.html', context)
