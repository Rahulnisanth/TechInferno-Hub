from django import forms
from django.forms import ModelForm
from .models import *

class ProjectForm(ModelForm):
      class Meta:
            model = Project
            fields = ['domain','title','description', 'featured_image', 'demo_link','source_link']
            widgets = {
                  'tags' : forms.CheckboxSelectMultiple(),
            }

      def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                  field.widget.attrs.update({'class':'input','placeholder':f"Add projects's {name} here"})


class ReviewForm(ModelForm):
      class Meta:
            model = Review
            fields = ['value', 'body']

            labels = {
                  'value':'Place your vote',
                  'body':'Add your comment with a vote',
            }
      
      def __init__(self, *args, **kwargs):
            super(ReviewForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                  field.widget.attrs.update({'class':'input'})