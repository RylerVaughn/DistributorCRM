# Generated by Django 5.1.6 on 2025-03-16 16:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0003_alter_messages_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
