# Generated by Django 5.1.6 on 2025-03-16 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 16, 0, 18, 21, 261501, tzinfo=datetime.timezone.utc)),
        ),
    ]
