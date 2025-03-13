from django.db import models

class Messages(models.Model):
    message_to = models.CharField(max_length=25)
    message_from = models.CharField(max_length=25)
    message_body = models.TextField()