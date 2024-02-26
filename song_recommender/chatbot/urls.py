# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
    # Add more URLs as needed
]
# chatbot/urls.py
from django.urls import path
from .views import chatbot_view

urlpatterns = [
    path('', chatbot_view, name='chatbot_view'),
    # Add more URLs as needed
]
