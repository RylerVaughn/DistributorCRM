from django.urls import path
from . import views

app_name = 'MessageForm'
urlpatterns = [
    path('', views.index, name='index'),
    path('createmessage/', views.create_message, name='createmessage'),
    path('viewmessages/', views.view_messages, name='viewmessages'),
    path('editmessage/<int:id>/', views.edit_message, name='editmessage'),
]