from django import forms
from django.forms import ModelForm
from .models import *


class ProjectForm(ModelForm):
    featured_image = forms.FileField(
        widget=forms.FileInput(attrs={"onchange": "previewImage(this)"})
    )

    class Meta:
        model = Project
        fields = [
            "featured_image",
            "domain",
            "title",
            "description",
            "completed_date",
            "demo_link",
            "source_link",
            "video",
        ]

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "input",
                    "placeholder": f"Add projects's {name} here",
                }
            )


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["body"]
        labels = {
            "body": "Add your comments for the above project :",
        }
        widgets = {
            "body": forms.Textarea(attrs={"rows": 5, "cols": 5}),
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "required": True})
