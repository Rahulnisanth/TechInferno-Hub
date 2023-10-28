from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from django.contrib.auth.models import User 
from .models import *

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
      if created:
            user = instance
            profile = Profile.objects.create(
                  user=user,
                  username=user.username,
                  email=user.email,
            )


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
      user = instance.user
      user.delete()
