from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ClientCreator, Client

def index(request):
    return render(request, 'CForm/index.html')

def create(request):
    if request.method == 'POST':
        form = ClientCreator(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CForm:index')
    else:
        form = ClientCreator()
        return render(request, 'CForm/create.html', context={'form': form})
    return HttpResponse('Error')

def view_clients(request):
    return render(request, 'CForm/viewclients.html', context={'clients': Client.objects.all()})

def view_specific(request, id):
    return render(request, 'CForm/viewspecific.html', context={'client': Client.objects.get(id=id)})