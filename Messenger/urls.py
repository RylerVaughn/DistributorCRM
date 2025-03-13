from django.urls import path
from . import views

app_name = "Messenger"
urlpatterns = [
    path("", views.index, name='index')
]