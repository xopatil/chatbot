# chatbot/views.py
import requests
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserProfileForm, CustomAuthenticationForm
from .models import UserProfile
from textblob import TextBlob
from django.http import JsonResponse
from .models import UserMessage
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chatbot_view')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required

# chatbot/views.py

def lastfm_api_request(artist, title):
    lastfm_api_key = 'your_lastfm_api_key'
    url = f'http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist={artist}&track={title}&api_key={lastfm_api_key}&format=json'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Extract and return relevant information from the API response
        return data['similartracks']['track'] if 'similartracks' in data else []
    else:
        # Handle API error
        return []

# chatbot/views.py


def analyze_tone(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Adjust as needed based on your requirements

# In your view function, you can use this function like:



# In your view function, you can use this function like:
def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_message', '')

        # Perform sentiment analysis using TextBlob
        analysis = TextBlob(user_input)
        sentiment_polarity = analysis.sentiment.polarity

        # Determine sentiment label based on polarity
        if sentiment_polarity > 0:
            sentiment_label = "Positive"
        elif sentiment_polarity < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        # You can customize the chatbot response based on the sentiment label
        if sentiment_label == "Positive":
            chatbot_response = "Great to hear that you're feeling positive!"
        elif sentiment_label == "Negative":
            chatbot_response = "I'm sorry to hear that you're feeling sed. How can I help you?"
        else:
            chatbot_response = "Neutral response from the chatbot."

        # Prepare the response data
        response_data = {
            'user_input': user_input,
            'sentiment_label': sentiment_label,
            'sentiment_polarity': sentiment_polarity,
            'chatbot_response': chatbot_response,
        }

        return JsonResponse(response_data)

    return render(request, 'chatbot/chatbot.html')

# chatbot/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is the chatbot home page.")
