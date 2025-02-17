from django.db import models
import django.forms as forms

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class ClientCreator(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number', 'address']
