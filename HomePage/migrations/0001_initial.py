# Generated by Django 5.1.6 on 2025-03-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_to', models.CharField(max_length=25)),
                ('message_from', models.CharField(max_length=25)),
                ('message_body', models.TextField()),
            ],
        ),
    ]
