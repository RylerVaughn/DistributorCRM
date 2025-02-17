from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MessageTemplateCreator, MessageTemplate

def index(request):
    return render(request, 'MessageForm/index.html')

def create_message(request):
    if request.method == 'POST':
        form = MessageTemplateCreator(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MessageForm:index')
    else:
        form = MessageTemplateCreator()
        return render(request, 'MessageForm/createmessage.html', context={'form': form})
    return HttpResponse('Error')

def view_messages(request):
    return render(request, 'MessageForm/viewmessages.html', context={'messages': MessageTemplate.objects.all()})

