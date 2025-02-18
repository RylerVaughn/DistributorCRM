from django.urls import path
from . import views

app_name = 'JobForm'
urlpatterns = [
    path('', views.index, name='index'),
]
