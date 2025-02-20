from django.db import models
import django.forms as forms
from CForm.models import Client

class Job(models.Model):
    date = models.DateField()
    job_payment = models.DecimalField(max_digits=5, decimal_places=2)
    job_tip = models.DecimalField(max_digits=5, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def total_payment(self):
        return f'${self.job_payment + self.job_tip}'

    def __str__(self):
        return f'Job Completed: {self.date}, Job Payment: {self.job_payment}, Job Tip: {self.job_tip}, Client: {self.client}'
    
class JobCreator(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['date', 'job_payment', 'job_tip', 'client']
