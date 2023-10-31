from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from django.contrib.auth.models import User 
from .models import *
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
      if created:
            user = instance
            profile = Profile.objects.create(
                  user=user,
                  username=user.username,
                  email=user.email,
            )
            # Email config ->
            subject = f'ProjectCaster welcomes you Mr/Mrs {profile.username}!'
            message = "Lorem ipsum is a placeholder text commonly used in the publishing and typography industries to demonstrate the layout and formatting of a document without revealing any actual content. Lorem ipsum is a placeholder text commonly used in the publishing and typography industries to demonstrate the layout and formatting of a document without revealing any actual content."
            send_mail(
                  subject,
                  message,
                  settings.EMAIL_HOST_USER,
                  [profile.email],
                  fail_silently=False
            )


@receiver(post_save, sender=Profile)
def updateProfile(sender, instance, created, **kwargs):
      profile = instance
      user = profile.user
      if created == False:
            user.username = profile.username
            user.email = profile.email
            user.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
      user = instance.user
      user.delete()
