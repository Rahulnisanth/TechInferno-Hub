from django.db import models
import uuid
from user.models import Profile
from django.contrib.auth.models import User


class Blog(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="images/default.png", upload_to="blog_images/"
    )
    upvotes = models.IntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.title

    @property
    def reviewers(self):
        reviewers = self.comment_set.all().values_list("owner__id", flat=True)
        return reviewers

    @property
    def getVotetotal(self):
        comments = self.comment_set.all()
        upVotes = comments.filter(value="up").count()
        self.vote_total = upVotes
        self.save()


class Comment(models.Model):
    VOTE_TYPE = (("up", "UpVote"),)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(
        max_length=200, default=None, blank=False, choices=VOTE_TYPE
    )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.value

    class Meta:
        unique_together = [["owner", "blog"]]
