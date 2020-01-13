
from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL
from phonenumber_field.modelfields import PhoneNumberField

class Event(models.Model):
    EventId                 = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False,null=False)
    EventName               = models.CharField(max_length = 50)
    Description             = models.TextField(max_length = 3000 )
    Image                   = models.ImageField(upload_to = 'images/')
    Event_Date              = models.DateField()
    EVENT_TYPE_CHOICES      = (
        ('PB', 'Public'),
        ('PR', 'Private'),
    )
    Event_type              = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES , default ='PB' )
    Participants_Limit      = models.IntegerField(default=5)
    created_by              = models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.EventName

class Participant(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    event                   = models.ManyToManyField(Event ,related_name='participants')
    Participation_date      = models.DateField()
    mobileno                = PhoneNumberField(default='')
    location                = models.CharField(max_length = 264)

    def __str__(self):
        return self.user.username

    def get_event(self):
        return ",".join([str(p) for p in self.event.all()])
