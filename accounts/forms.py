# users/forms.py
from django import forms
from accounts.models import Participant,Event
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    class Meta():
        model = Event
        fields = '__all__'

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

    def clean(self):
        all = super().clean()
        for event in all['event']:
            if event.participants.count() >= event.Participants_Limit:
                raise forms.ValidationError("Registrations are closed.")
            elif event.Event_Date != data['Participation_date']:
                raise forms.ValidationError("Participation_date should match with the Event_Date. ")
            else:
                event_obj = Event.objects.all()
                for event in event_obj:
                    for participant in event.participants.all():
                        if participant.Participation_date == data['Participation_date'] and participant.user == data['user']:
                            raise forms.ValidationError("Registration Failed,because You have already registered for some other event on the same day.")
