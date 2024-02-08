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
        subject = "Welcome to TechInferno Hub"
        message = f"""Dear {profile.username},

Greetings from the TechInferno Hub team! We are thrilled to welcome you to our dynamic community dedicated to showcasing groundbreaking projects and cutting-edge techWorks. As a passionate advocate for innovation and technological advancements, we are excited to have you on board.

At TechInferno, we believe in the power of ideas and the impact they can have on the world. Whether you're a seasoned professional, a budding enthusiast, or someone with a keen interest in the latest technological marvels, our platform is designed to inspire, connect, and elevate your experience.

Here's what you can look forward to:
1. Explore Innovative Projects: Dive into a curated collection of remarkable projects spanning various industries and technologies. From AI and robotics to sustainable energy solutions, our platform is a hub for the latest and greatest innovations.
2. Showcase Your TechWorks: Are you working on a groundbreaking project? We invite you to share your techWorks with our community. Be a part of the conversation, get feedback, and connect with like-minded individuals who share your passion for pushing the boundaries of what's possible.
3. Personalized Experience: Tailor your [Your Website Name] experience to your interests. Our platform is designed to understand your preferences, ensuring you receive content and recommendations that align with your tech interests.

To get started:
- Create Your Profile: Complete your profile to connect with fellow innovators and enthusiasts.
- Explore Projects: Start browsing through our diverse collection of projects for inspiration.
- Share Your Work: Showcase your own techWorks and be part of a community that celebrates innovation.

We're on a mission to create a collaborative space that fosters creativity, learning, and advancement in the world of technology. Thank you for joining us on this exciting journey.


Best Regards,
@The Team TechInferno """

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
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
    try:
        user = instance.user
        user.delete()
    except:
        pass
