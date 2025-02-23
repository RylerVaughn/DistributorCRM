from django.db import models
from django import forms as forms
from MessageForm.models import MessageTemplate
from CForm.models import Client

class MessageHistory(models.Model):
    message_template = models.ForeignKey(MessageTemplate, on_delete=models.SET_NULL, null=True)
    clients = models.ManyToManyField(Client, related_name='messages')

class MessageHistoryCreator(forms.ModelForm):
    class Meta:
        model = MessageHistory
        fields = ['message_template', 'clients']