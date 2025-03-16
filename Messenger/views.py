from django.shortcuts import render
from django.http import HttpResponse
from CForm.models import Client
from .services.Messenger.message_api import TextMessageApi

# Index is the only view in here, it is just to show all of the messages with clients.
def index(request):

    text_api = TextMessageApi()

    return render(request, "Messenger/index.html", context={'conversations': text_api.get_conversations()})