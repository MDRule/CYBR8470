from django.contrib import admin
from .models import Event, Participation, Profile, Feedback  # Ensure Profile is imported


# Register Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'created_at')  # Ensure these fields exist
    search_fields = ('name', 'description')
# Register Participation model
@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'timestamp')
    search_fields = ('user__username', 'event__name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'get_phone_number')  # Use a callable instead of 'phone_number'

    def get_phone_number(self, obj):
        return obj.phone_number
    get_phone_number.short_description = 'Phone Number'  # Customize column header


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('get_event_name', 'feedback')  # Use a method to display event name

    def get_event_name(self, obj):
        return obj.event.name  # Access the related event's name
    get_event_name.short_description = 'Event Name'  # Label for the column