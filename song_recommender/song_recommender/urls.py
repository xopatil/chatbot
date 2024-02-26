# song_recommender/urls.py
from django.contrib import admin
from django.urls import path, include
from chatbot.views import chatbot_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),
    path('', chatbot_view, name='chatbot_view'),  # Display the chatbot by default
]

