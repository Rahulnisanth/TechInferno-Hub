from django import forms
from django.forms import ModelForm
from .models import *


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "domain",
            "title",
            "description",
            "featured_image",
            "demo_link",
            "project_documentation",
            "source_link",
        ]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != "demo_link" or name != "project_documentation":
                field.widget.attrs.update(
                    {
                        "class": "input",
                        "placeholder": f"Add projects's {name} here",
                        "required": True,
                    }
                )
            else:
                field.widget.attrs.update(
                    {"class": "input", "placeholder": f"Add projects's {name} here"}
                )


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["value", "body"]

        labels = {
            "value": "Place your votes here :",
            "body": "Add your comment with an endorsement",
        }
        widgets = {
            "value": forms.RadioSelect(),
            "body": forms.Textarea(attrs={"rows": 5, "cols": 5}),
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "required": True})
