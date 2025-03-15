from django.shortcuts import render
from django.http import HttpResponse
from CForm.models import Client

# Index is the only view in here, it is just to show all of the messages with clients.
def index(request):
    return render(request, "Messenger/index.html", context={'clients': list(Client.objects.values())})