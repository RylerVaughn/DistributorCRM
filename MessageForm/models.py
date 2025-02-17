from django.db import models
import django.forms as forms

# Create your models here.

class MessageTemplate(models.Model):
    body = models.TextField()

    def __str__(self):
        return f'{self.body}'

class MessageTemplateCreator(forms.ModelForm):
    class Meta:
        model = MessageTemplate
        fields = ['body']