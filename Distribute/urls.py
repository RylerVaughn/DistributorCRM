from django.urls import path
from . import views

app_name = 'Distribute'
urlpatterns = [
    path('', views.index, name='index'),
    path('selectmessage/', views.select_message, name='selectmessage'),
    path('selectclients/', views.select_clients, name='selectclients'),
]