# chatbot/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional user profile fields if needed

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    # Add more fields as needed
class UserMessage(models.Model):
    message = models.TextField()
    sentiment_label = models.CharField(max_length=10)
    sentiment_polarity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    