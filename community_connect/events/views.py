from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Event, Participation
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    return HttpResponse("Welcome to Community Connect!")

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_signup(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Participation.objects.create(user=request.user, event=event)
    return redirect('event_list')

# events/views.py
def my_participation(request):
    participations = Participation.objects.filter(user=request.user)
    return render(request, 'events/my_participation.html', {'participations': participations})

class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'description', 'date']
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = Event
    fields = ['name', 'description', 'date']
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('event_list')

def view_signups(request, event_id):
    participations = Participation.objects.filter(event_id=event_id)
    return render(request, 'events/view_signups.html', {'participations': participations})


def approve_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.status = 'Approved'
    event.save()
    return redirect('admin_dashboard')