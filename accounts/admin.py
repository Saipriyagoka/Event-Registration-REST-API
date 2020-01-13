# users/admin.py
from django.contrib import admin
from accounts.forms import ParticipantForm,EventForm
from accounts.models import Participant,Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['EventName', 'Event_Date', 'Event_type','Participants_Limit']

admin.site.register(Event,EventAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    form = ParticipantForm
    list_display = ['user', 'get_event','Participation_date','location']

admin.site.register(Participant,ParticipantAdmin)
