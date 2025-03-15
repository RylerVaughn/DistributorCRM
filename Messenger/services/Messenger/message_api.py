from twilio.rest import Client
from HomePage.models import Messages
import os
from text_message_objects import TextMessage

# on startup this function will query the twilio database and retrieve any inbound messages that were sent while the program was offline.
def grab_message_database():
    client = get_twilio_client()
    message_list = client.messages.list()
    # check our message database for new values based on the SID, catch them if found.
    try:
        for message in message_list:
            Messages.objects.create(
                message_sid=message.sid,
                message_to=message.to,
                message_from=message.from_,
                message_body=message.body,
                message_date=message.date_created,
            )
    except:
        print("Duplicate message found and caught.")
    
# "Conversations" dictionary, keys are clients phone number and values are the list of messages throughout the entire history with that person.
def get_sorted_messages() -> dict:
    conversations = {}
    my_number = "+18127821348"
    for message in Messages.objects.all().order_by("message_date"):
        # get the unique number into this variable so that we can format the keys by it.
        unique_number = message.message_from if message.message_from != my_number else message.message_to

        if unique_number not in conversations:
            conversations[unique_number] = []

        text_message = TextMessage(message.message_from, message.message_to, message.message_body)

        conversations[unique_number].append(text_message)

    return conversations

# return twilio client to keep DRY.
def get_twilio_client():
    return Client(
        os.getenv("TWILIO_STR_IDENTIFIER"),
        os.getenv("TWILIO_AUTH_TOKEN"),
    )