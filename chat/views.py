from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime

# In-memory chat storage no DB
CHAT_ROOMS = {}

# Rendering chat room on this one
def chat_room(request, room):
    return render(request, "chat/room.html", {"room": room})


# Returning messages as JSON
def get_messages(request, room):
    messages = CHAT_ROOMS.get(room, [])
    return JsonResponse(messages, safe=False)


# Handling POST requests to save messages
def post_message(request, room):
    if request.method == "POST":
        username = request.POST.get("username", "Anonymous")
        content = request.POST.get("content")

        if content:
            CHAT_ROOMS.setdefault(room, []).append(
                {"username": username, "content": content, "timestamp": datetime.now().strftime("%H:%M:%S")}
            )

    return JsonResponse({"status": "ok"})
