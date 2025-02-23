from django.shortcuts import render, redirect
from MessageForm.models import MessageTemplate
from CForm.models import Client
from .models import MessageHistory, MessageHistoryCreator

def index(request):
    text_message = request.session.get('text_message', '')
    text_message = MessageTemplate.objects.get(id=text_message)
    client_ids = request.session.get('client_list', '')
    client_list = [Client.objects.get(id=int(client_id)) for client_id in client_ids]
    return render(request, 'Distribute/index.html', context={'text_message': text_message, 'client_list': client_list})

def select_message(request):
    if request.method == 'POST':
        text_message = request.POST.get('text_message')
        request.session['text_message'] = text_message
        return redirect('Distribute:index')
    return render(request, 'Distribute/selectmessage.html', context={'messages': MessageTemplate.objects.all()})

def select_clients(request):
    if request.method == "POST":
        client_list = request.POST.getlist('client-checkbox')
        request.session['client_list'] = client_list
        return redirect('Distribute:index')
    return render(request, 'Distribute/selectclients.html', context={'clients': Client.objects.all()})

