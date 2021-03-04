from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile,Post
class user_registeration_form(UserCreationForm):
    email=forms.EmailField()
    name=forms.CharField()
    class Meta:
        model=User
        fields=['name','username','password1','password2','email']
class photos(forms.ModelForm):
    class Meta:
        model=profile
        fields=['image']
class posts(forms.ModelForm):
    class Meta:
        model=Post
        fields=['topic','post','introduction','title']
