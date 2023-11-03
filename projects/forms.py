from django import forms
from django.forms import ModelForm
from .models import *

class ProjectForm(ModelForm):
      class Meta:
            model = Project
            fields = ['domain','title','description', 'featured_image', 'project_documentation', 'demo_link','source_link']
            widgets = {
                  'tags' : forms.CheckboxSelectMultiple(),
            }

      def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                  if name != 'demo_link' or name != 'project_documentation':
                        field.widget.attrs.update({'class':'input','placeholder':f"Add projects's {name} here", 'required':True})
                  else:
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
                  field.widget.attrs.update({'class':'input', 'required':True})