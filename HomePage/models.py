from django.db import models
from django.utils import timezone

class Messages(models.Model):
    message_sid = models.CharField(max_length=150, null='Undefined.')
    message_to = models.CharField(max_length=25)
    message_from = models.CharField(max_length=25)
    message_body = models.TextField()
    message_date = models.DateTimeField(default=timezone.now)
