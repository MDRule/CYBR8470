from django.contrib import admin

# Register your models here.

from .models import Event, Participation

# Register Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'created_at')
    search_fields = ('name', 'description')

# Register Participation model
@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'timestamp')
    search_fields = ('user__username', 'event__name')
