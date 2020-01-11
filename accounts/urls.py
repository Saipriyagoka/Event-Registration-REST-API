from django.urls import path
from accounts.views import *
from django.views.generic.base import TemplateView

urlpatterns = [
#    path('userRegistraion/', APIUserCreateView.as_view(), name="userregister"),
    path('signup/', SignUp.as_view(), name='signup'),
    path('eventList/', APIEventListView.as_view() , name='list'),
    path('createEvent/', APIEventCreateView.as_view() , name='create'),
    path('participantList/', APIParticipantListView.as_view() , name='createParticipant'),
    path('eventRegistration/', APIParticipantCreateView.as_view() , name='register'),
    path('deleteEvent/<uuid:pk>/delete/', APIEventDeleteView.as_view(), name='Eventdelete'),
    path('unRegister/<int:pk>/delete/', APIParticipantDeleteView.as_view(), name='ParticipantDelete'),
    path('eventRetrieve/<str:EventName>/', APIEventRetrieveView.as_view(), name='apiretrieve'),
    #path('retrieve/<str:EventName>/', EventRetrieveView, name='retrieve'),
    #path('register/<str:EventName>/', EventRegistration, name='register'),
    #path('Eventcreate', EventCreation, name='createEvent'),
]
