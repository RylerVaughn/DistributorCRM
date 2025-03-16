import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Distributor.settings')

# Step 2: Initialize Django
django.setup()

from Messenger.services.Messenger.message_api import TextMessageApi

api = TextMessageApi()
conversations = api.get_conversations()
