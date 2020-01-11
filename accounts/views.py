
from django.shortcuts import render,get_object_or_404,HttpResponse,redirect,render_to_response
from rest_framework.response import Response
from django.core import serializers
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework import status

from accounts.models import Event , Participant , Account
from accounts.serializers import EventSerializer ,ParticipantSerializer
from accounts.forms import EventForm , ParticipantForm
from django.contrib.auth.models import User

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class APIEventListView(generics.ListAPIView):
    queryset = Event.objects.filter(Event_type = 'PB')
    serializer_class = EventSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'ListEvent.html'

    def get(self, *args, **kwargs):
        queryset1 = Event.objects.filter(Event_type = 'PB')
        return Response({'EventList_obj' : queryset1})

class APIEventCreateView(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'EventCreation.html'

    def get(self, request):
        serializer=EventSerializer
        return Response({'serializer':serializer})

    def post(self, request):
        serializer = EventSerializer(data=self.request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('list')

class APIEventRetrieveView(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'EventName'
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Eventview.html'

    def get(self, request, EventName):
         queryset1 = self.get_object()
         det = Event.objects.all()
         serializer = EventSerializer(queryset1)

         return Response({'EventRetrieve_obj' : serializer.data ,'abc':det})

class APIEventDeleteView(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class APIParticipantListView(generics.ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class APIParticipantCreateView(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'EventRegistration.html'

    def get(self, request):
        serializer=ParticipantSerializer
        return Response({'serializer':serializer})

    def post(self, request):
        serializer = ParticipantSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('list')

class APIParticipantDeleteView(generics.DestroyAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
