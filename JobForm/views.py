from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Job, JobCreator
from CForm.models import Client

def index(request):
    return render(request, 'JobForm/index.html')

def add_job(request):
    if request.method == 'POST':
        form = JobCreator(request.POST)
        if form.is_valid():
            form.save()
            return redirect('JobForm:index')
    else:
        form = JobCreator()
    return render(request, 'JobForm/addjob.html', context={'form': form, 'clients': Client.objects.all()})