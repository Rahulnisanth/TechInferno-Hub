from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
      class Meta:
            model = User
            fields = ['username','email','password1','password2',]
            labels = {
                  'password1': 'Password',
                  'password2' : 'Password Confirmation',
            }
      def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                  field.widget.attrs.update({'class':'input'})



class ProfileForm(ModelForm):
      class Meta:
            model = Profile
            fields = ['username', 'profile_picture', 'email','location', 'job_role', 'short_intro', 'bio', 'website', 'github', 'stackoverflow','linkedin','twitter']

      def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)

            for name,field in self.fields.items():
                  field.widget.attrs.update({'class':'input'})
      

class SkillForm(ModelForm):
      class Meta:
            model = Skill
            fields = '__all__'
            exclude = ['owner']

      def __init__(self, *args, **kwargs):
            super(SkillForm, self).__init__(*args, **kwargs)

            for name,field in self.fields.items():
                  field.widget.attrs.update({'class':'input'})
