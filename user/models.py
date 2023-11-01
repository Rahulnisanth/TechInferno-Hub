from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
      user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
      profile_picture = models.ImageField(null=True, blank=True, default='images/default__profile.png', upload_to='profile__picture/')
      username = models.CharField(max_length=200, null=True, blank=True)
      location = models.CharField(max_length=200, null=True, blank=True)
      job_role = models.CharField(max_length=200, null=True, blank=True)
      email = models.CharField(null=True, blank=True, max_length=150)
      short_intro = models.CharField(null=True, blank=True, max_length=1000)
      bio = models.TextField(null=True, blank=True, max_length=2000)
      website = models.CharField(max_length=500, null=True, blank=True)
      github = models.CharField(max_length=500, null=True, blank=True)
      stackoverflow = models.CharField(max_length=500, null=True, blank=True)
      linkedin = models.CharField(max_length=500, null=True, blank=True)
      twitter = models.CharField(max_length=500, null=True, blank=True)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

      def __str__(self):
            return str(self.user.username)

      @property
      def ImageURL(self):
            try:
                  url = self.profile_picture.url
            except:
                  url = 'media/images/default__profile.png'
            return url
      class Meta:
            ordering = ['-created']


class Skill(models.Model):
      owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
      name = models.CharField(max_length=200, null=True, blank=True)
      description = models.TextField(max_length=1000, null=True, blank=True)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

      def __str__(self):
            return str(self.name)
      
class Message(models.Model):
      sender = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
      receiver = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE, related_name='messages')
      name = models.CharField(max_length=200, null=True, blank=True)
      subject = models.CharField(max_length=500, null=True, blank=True)
      body = models.TextField(max_length=3000, null=True, blank=True)
      is_read = models.BooleanField(default=False, null=True)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

      def __str__(self):
            return self.name

      class Meta:
            ordering = ['is_read','-created']
      
