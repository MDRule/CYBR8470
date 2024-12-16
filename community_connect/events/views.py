# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden
from .models import Event, Participation
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import VolunteerSignupForm, EventForm, FeedbackForm
from django.contrib.auth.decorators import login_required



def home(request):
    return HttpResponse("Welcome to Community Connect!")

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_signup(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Participation.objects.create(user=request.user, event=event)
    return redirect('event_list')

def my_participation(request):
    participations = Participation.objects.filter(user=request.user)
    return render(request, 'events/my_participation.html', {'participations': participations})

class CreateEventView(CreateView):
    model = Event
    fields = ['name', 'description', 'date']
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('browse_events')

class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'description', 'date']
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('browse_events')


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

#def browse_events(request):
#    events = Event.objects.all().order_by('date')  # Show events in chronological order
#    return render(request, 'events/browse_events.html', {'events': events})
def browse_events(request):
    events = Event.objects.all()
    return render(request, 'events/browse_events.html', {'events': events})
def manage_events(request):
    events = Event.objects.filter(status='Pending')
    return render(request, 'events/manage_events.html', {'events': events})



def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('browse_events')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

def browse_events(request):
    events = Event.objects.all()
    return render(request, 'events/browse_events.html', {'events': events})


def volunteer_signup(request):
    if request.method == 'POST':
        form = VolunteerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browse_events')
    else:
        form = VolunteerSignupForm()
    return render(request, 'events/volunteer_signup.html', {'form': form})


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('browse_events')
    else:
        form = FeedbackForm()
    return render(request, 'events/feedback.html', {'form': form})