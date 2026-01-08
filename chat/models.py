from django.db import models

# My Ajax chat message model


class Message(models.Model):
    username = models.CharField(max_length=50)  # sender
    content = models.TextField()  # message body
    timestamp = models.DateTimeField(auto_now_add=True)  # time when was sent

    def __str__(self):
        return f"{self.username}: {self.content}"
