from django import forms
from django.forms import ModelForm
from .models import *


class BlogForm(ModelForm):
    featured_image = forms.FileField(
        widget=forms.FileInput(attrs={"onchange": "previewImage(this)"})
    )

    class Meta:
        model = Blog
        fields = [
            "featured_image",
            "title",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "input",
                    "placeholder": f"Add blog's {name} here",
                }
            )


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]

        labels = {
            "body": "Add your comments for the above blog here :",
        }
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 4,
                    "cols": 5,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "required": True})
