from rest_framework import serializers
from accounts.models import Participant,Event


class ParticipantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Participant
		fields = '__all__'
		read_only_fields = ('user','Participation_date','event',)

	def create(self, validated_data):
		request = getattr(self.context, 'request', None)
		EventName = getattr(self.context, 'EventName', None)
		event_details = Event.objects.get(EventName =self.context['EventName'])
		if 'user' not in validated_data:
			validated_data['user'] = self.context['request'].user
		if 'Participation_date' not in validated_data:
			validated_data['Participation_date'] = event_details.Event_Date
		eventdetails = Event.objects.filter(EventName =self.context['EventName'])
		if 'event' not in validated_data:
			validated_data['event'] = eventdetails
		return super(ParticipantSerializer, self).create(validated_data)

	def validate(self, data):
		request = getattr(self.context, 'request', None)
		EventName = getattr(self.context, 'EventName', None)
		event_details = Event.objects.get(EventName =self.context['EventName'])
		if event_details.participants.count() >= event_details.Participants_Limit:
			raise serializers.ValidationError({'location' :"Registrations are closed." })
		else:
			event_obj = Event.objects.all()
			for event in event_obj:
				for participant in event.participants.all():
					if participant.Participation_date == event_details.Event_Date and participant.user == self.context['request'].user:
						raise serializers.ValidationError({'location' :"Registration Failed,because You have already registered for some other event on the same day."})
		return data

class EventSerializer(serializers.ModelSerializer):
	participants = ParticipantSerializer(many=True, read_only=True)

	class Meta:
		model = Event
		fields = '__all__'
		read_only_fields = ('created_by',)

	def create(self, validated_data):
		if 'created_by' not in validated_data:
			request = getattr(self.context, 'request', None)
			validated_data['created_by'] = self.context['request'].user
		return super(EventSerializer, self).create(validated_data)
