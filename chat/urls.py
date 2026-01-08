from django.urls import path

# Multiple chats enabled
from . import views

urlpatterns = [
    path("<str:room>/", views.chat_room),  # main chat page
    path("<str:room>/get_messages/", views.get_messages),  # fetch messages
    path("<str:room>/post_message/", views.post_message),  # send message
]
