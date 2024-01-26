from django.db import models
import uuid
from user.models import Profile
from django.contrib.auth.models import User


class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    domain = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="images/default.png", upload_to="images/"
    )
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    completed_date = models.DateField(null=True, blank=True)
    favorite = models.ManyToManyField(User, related_name="favorite", blank=True)
    like = models.ManyToManyField(Profile, related_name="like_count")
    tags = models.ManyToManyField("Tag", blank=True)
    view_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    class Meta:
        ordering = ["-view_count"]

    @property
    def reviewers(self):
        reviewers = self.review_set.all().values_list("owner__id", flat=True)
        return reviewers

    @property
    def ImageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = "static/images/default__blog.jpg"
        return url

    def __str__(self) -> str:
        return str(self.title)


class Review(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    class Meta:
        unique_together = [["owner", "project"]]

    def __str__(self) -> str:
        return str(self.project)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return str(self.name)


class ProjectView(models.Model):
    post = models.ForeignKey(Project, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("post", "session_key", "ip_address")

    def __str__(self) -> str:
        return str(self.session_key)
