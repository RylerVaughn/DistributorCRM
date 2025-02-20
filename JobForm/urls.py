from django.urls import path
from . import views

app_name = 'JobForm'
urlpatterns = [
    path('', views.index, name='index'),
    path('addjob/', views.add_job, name='addjob'),
    path('viewjobs/', views.view_jobs, name='viewjobs'),
    path('editjob/<int:id>/', views.edit_job, name='editjob')
]
