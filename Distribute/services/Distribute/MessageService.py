from twilio.rest import Client
import os

# High level function used specifically for django views. Made for decoding message templates and routing it to all clients provided.
def SendTextMessages(client_list: list, message_template: str):
    for client in client_list:
        send_message(client, message_template)

    # Create internal function for decoding message templates here.

def send_message(client, text_message: str):
    message_client = get_message_client()
    try:
        message_client.messages.create(
            from_='+18127821348',
            body=text_message,
            to=client.phone_number
        )
    except Exception as e:
        print(f"Error Occured: {str(e)}")

def get_message_client() -> Client:
    return Client(
        os.getenv("TWILIO_STR_IDENTIFIER"),
        os.getenv("TWILIO_AUTH_TOKEN")
    )