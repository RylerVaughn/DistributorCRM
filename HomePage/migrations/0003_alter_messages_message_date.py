# Generated by Django 5.1.6 on 2025-03-16 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_messages_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 16, 0, 18, 51, 257551, tzinfo=datetime.timezone.utc)),
        ),
    ]
