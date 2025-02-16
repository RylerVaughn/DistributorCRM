from django.urls import path
from . import views

app_name = 'CForm'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('viewclients/', views.view_clients, name='viewclients'),
    path('viewspecific/<int:id>/', views.view_specific, name='viewspecific'),
    path('editclient/<int:id>/', views.edit_client, name='editclient'),
]