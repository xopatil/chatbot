# chatbot/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CustomAuthenticationForm(AuthenticationForm):
    # Customize authentication form if needed
    pass
