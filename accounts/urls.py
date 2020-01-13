from django.urls import path
from accounts.views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('eventList/', APIEventListView.as_view() , name='list'),
    path('createEvent/', APIEventCreateView.as_view() , name='create'),
    path('participantList/', APIParticipantListView.as_view() , name='createParticipant'),
    path('eventRegistration/<str:EventName>/', APIParticipantCreateView.as_view() , name='register'),
    path('deleteEvent/<uuid:EventId>/delete/', APIEventDeleteView, name='Eventdelete'),
    path('unRegister/<int:id><str:EventName>/delete/', APIParticipantDeleteView, name='ParticipantDelete'),
    path('eventRetrieve/<str:EventName>/', APIEventRetrieveView.as_view(), name='apiretrieve'),
]
