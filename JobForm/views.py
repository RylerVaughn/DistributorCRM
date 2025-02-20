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

def view_jobs(request):
    return render(request, "JobForm/viewjobs.html", context={'jobs': Job.objects.all()})

def edit_job(request, id):
    instance = Job.objects.get(pk=id)
    if request.method == "POST":
        action = request.POST.get('_action')
        if action == 'delete':
            instance.delete()
            return redirect('JobForm:viewjobs')
        elif action == 'update':
            form = JobCreator(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('JobForm:viewjobs')
    else:
        form = JobCreator()
        return render(request, 'JobForm/editjob.html', context={'job': instance, 'form': form, 'clients': Client.objects.all()})
