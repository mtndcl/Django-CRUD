from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver

from PIL import Image
from datetime import datetime

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
		
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True,null=True)
	location = models.CharField(max_length=30, blank=True,null=True)
	birth_date = models.DateField(null=True, blank=True)
	image = models.ImageField(default='default.jpg', upload_to='images/')






@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
	
	posttext=models.TextField(max_length=100, blank=True,null=True)
	date=models.DateTimeField(default=datetime.now())
	image = models.ImageField(null=True, upload_to='images/')
	