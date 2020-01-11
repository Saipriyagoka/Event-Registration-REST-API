from rest_framework import serializers
from accounts.models import Participant,Event

class ParticipantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Participant
		fields = '__all__'

	def validate(self, data):
		for event in data['event']:
			if event.participants.count() >= event.Participants_Limit:
				raise serializers.ValidationError({'event':"Registrations are closed." })
			elif event.Event_Date != data['Participation_date']:
				raise serializers.ValidationError({'Participation_date':"Participation_date should match with the Event_Date. "})
			else:
				event_obj = Event.objects.all()
				for event in event_obj:
					for participant in event.participants.all():
						if participant.Participation_date == data['Participation_date'] and participant.user == data['user']:
							raise serializers.ValidationError({'user':"Registration Failed,because You have already registered for some other event on the same day."})
		return data

class EventSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
