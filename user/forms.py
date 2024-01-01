from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
        labels = {
            "password1": "Password",
            "password2": "Password Confirmation",
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "required": True})


class ProfileForm(ModelForm):
    profile_picture = forms.FileField(
        widget=forms.FileInput(attrs={"onchange": "previewImage(this)"})
    )
    class Meta:
        model = Profile
        fields = [
            "profile_picture",
            "username",
            "email",
            "location",
            "job_role",
            "short_intro",
            "bio",
            "website",
            "github",
            "stackoverflow",
            "linkedin",
            "twitter",
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "required": True})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["name", "subject", "body"]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "required": True})
