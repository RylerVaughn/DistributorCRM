from django.urls import path
from . import views

app_name = 'JobForm'
urlpatterns = [
    path('', views.index, name='index'),
    path('addjob/', views.add_job, name='addjob'),
]
