# users/admin.py
from django.contrib import admin
from accounts.forms import ParticipantForm,EventForm
from accounts.models import Participant,Event

class EventAdmin(admin.ModelAdmin):
    
    list_display = ['EventName', 'Event_Date', 'Event_type','Participants_Limit']

# class EventAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         instance = EventForm.save(commit=False)
#         instance.created_by = request.user
#         instance.save()
#         EventForm.save_m2m()
#         return instance
#     list_display = ['EventName', 'Event_Date', 'Event_type','Participants_Limit']

admin.site.register(Event,EventAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    form = ParticipantForm
    #list_display = ['email', 'username', 'Event','Participation_date','Availability_status']

admin.site.register(Participant,ParticipantAdmin)
