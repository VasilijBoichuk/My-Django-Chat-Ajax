from django.http import JsonResponse
from django.shortcuts import render

from .models import Message


# Rendering chat room on this one
def chat_room(request):
    return render(request, "chat/room.html")


# Returning messages as JSON
def get_messages(request):
    messages = Message.objects.order_by("timestamp").all()
    data = [
        {
            "username": m.username,
            "content": m.content,
            "timestamp": m.timestamp.strftime("%H:%M:%S"),
        }
        for m in messages
    ]
    return JsonResponse(data, safe=False)


# Handling POST requests to save messages
def post_message(request):
    if request.method == "POST":
        username = request.POST.get("username", "Anonymous")
        content = request.POST.get("content")
        if content:
            Message.objects.create(username=username, content=content)
    return JsonResponse({"status": "ok"})
