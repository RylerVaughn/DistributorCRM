from twilio.rest import Client
from HomePage.models import Messages
import os
from CForm.models import Client as Clientel

class TextMessageApi():
    # on startup this function will query the twilio database and retrieve any inbound messages that were sent while the program was offline.
    def grab_message_database(self):
        client = self.get_twilio_client()
        message_list = client.messages.list()
        # check our message database for new values based on the SID, catch them if found.
        for message in message_list:
            try:
                Messages.objects.create(
                    message_sid=message.sid,
                    message_to=message.to,
                    message_from=message.from_,
                    message_body=message.body,
                    message_date=message.date_created,
                )
            except:
                print(f"Duplicate message found and caught.")
    
    # "Conversations" dictionary, keys are clients phone number and values are the list of messages throughout the entire history with that person.
    def get_sorted_messages(self) -> dict:
        conversations = {}
        my_number = "+18127821348"
        for message in Messages.objects.all().order_by("message_date"):
            # get the unique number into this variable so that we can format the keys by it.
            unique_number = message.message_from if message.message_from != my_number else message.message_to

            if unique_number not in conversations:
                conversations[unique_number] = []

            #previously used a TextMessage object but that cannot be transformed into a json object so I switch to a more primitive data structure.
            text_message = {
                'sender': message.message_from,
                'reciever': message.message_to,
                'body': message.message_body,
                'date': message.message_date,
                "sid": message.message_sid,
            }

            conversations[unique_number].append(text_message)

        return conversations

    # main method that view will call, calls on other methods to keep DRY.
    def get_conversations(self) -> dict:
        self.grab_message_database()
        raw_messages = self.get_sorted_messages()
        clients = list(Clientel.objects.all())
        conversations = self.merge_into_conversations(raw_messages, clients)
        return conversations

    # function for merging the messages with the clients into one dictionary, replacing the keys with a clients PK if a connection is found.
    def merge_into_conversations(self, messages: dict, clients: list) -> dict:
        for client in clients:
            if client.phone_number in messages:
                messages[f"{client.first_name} {client.last_name}"] = messages.pop(client.phone_number)

            else:
                messages[f"{client.first_name} {client.last_name}"] = []
        return messages

    # return twilio client to keep DRY.
    def get_twilio_client(self):
        return Client(
            os.getenv("TWILIO_STR_IDENTIFIER"),
            os.getenv("TWILIO_AUTH_TOKEN"),
        )