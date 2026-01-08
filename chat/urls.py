from django.urls import path

from . import views

urlpatterns = [
    path("", views.chat_room, name="chat_room"),  # main chat page
    path("get_messages/", views.get_messages, name="get_messages"),  # fetch messages
    path("post_message/", views.post_message, name="post_message"),  # send message
]
