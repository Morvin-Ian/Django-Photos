from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [ 'username','email', 'password1', 'password2']


class UpdateDetails(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [ 'username','email']

class UpdateProfile(forms.ModelForm):
   class Meta:
       model = Profile
       fields = ['profile_pic']
