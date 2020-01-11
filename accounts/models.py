# users/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.email

class Event(models.Model):
    EventId                 = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False,null=False)
    EventName               = models.CharField(max_length = 50)
    Description             = models.TextField(max_length = 3000 )
    Image                   = models.ImageField(upload_to = 'images/')
    Event_Date              = models.DateField(null=True)
    EVENT_TYPE_CHOICES      = (
        ('PB', 'Public'),
        ('PR', 'Private'),
    )
    Event_type              = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES , default ='PB' )
    Participants_Limit      = models.IntegerField(default=5)
    #created_by              = models.ForeignKey(settings.AUTH_USER_MODEL,default='',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.EventName

class Participant(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    #name                    = models.CharField(max_length = 50,unique = True)
    event                   = models.ManyToManyField(Event ,related_name='participants')
    Participation_date      = models.DateField(null=True)
    def __str__(self):
        return self.user.username

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Participant.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.participant.save()
