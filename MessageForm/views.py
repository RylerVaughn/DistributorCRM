from django.shortcuts import render, redirect, get_object_or_404
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

def edit_message(request, id):
    instance = get_object_or_404(MessageTemplate, pk=id)
    if request.method == 'POST':
        action = request.POST.get('_action')
        if action == 'delete':
            instance.delete()
            return redirect('MessageForm:viewmessages')
        elif action == 'update':
            form = MessageTemplateCreator(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('MessageForm:viewmessages')
    else:
        form = MessageTemplateCreator()
        return render(request, 'MessageForm/editmessage.html', context={'message': instance, 'form': form})


