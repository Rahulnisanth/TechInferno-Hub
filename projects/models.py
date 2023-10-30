from django.db import models
import uuid
from user.models import Profile

class Project(models.Model):
      owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
      title = models.CharField(max_length=200)
      domain = models.CharField(max_length=200, null=True, blank=True)
      description = models.TextField(null=True, blank=True)
      featured_image = models.ImageField(null=True, blank=True, default='images/default.png', upload_to='images/')
      demo_link = models.CharField(max_length=2000, null=True, blank=True)
      source_link = models.CharField(max_length=2000, null=True, blank=True)
      tags = models.ManyToManyField('Tag', blank=True)
      vote_total = models.IntegerField(default=0, blank=True, null=True)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

      def __str__(self) -> str:
            return self.title

      class Meta:
            ordering = ['-vote_total','title']
      
      @property
      def reviewers(self):
            reviewers = self.review_set.all().values_list('owner__id', flat=True)
            return reviewers
      @property
      def getVotetotal(self):
            reviews = self.review_set.all()
            upVotes = reviews.filter(value='up').count()
            self.vote_total = upVotes
            self.save()

class Review(models.Model):
      VOTE_TYPE = (
            ('up', 'up vote'),
            ('down', 'down vote'),
      )
      owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
      project = models.ForeignKey(Project, on_delete=models.CASCADE)
      body = models.TextField(null=True, blank=True)
      value = models.CharField(max_length=200, choices=VOTE_TYPE)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

      def __str__(self) -> str:
            return self.value

      class Meta:
            unique_together =[['owner','project']]

            
class Tag(models.Model):
      name = models.CharField(max_length=200)
      created = models.DateTimeField(auto_now_add=True)
      id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

      def __str__(self) -> str:
            return self.name
