from twilio.rest import Client
import os

# High level function used specifically for django views. Made for decoding message templates and routing it to all clients provided.
def SendTextMessages(client_list: list, message_template: str):
    
    # Create internal function for decoding message templates here.

    for client in client_list:
        send_message(client, message_template)

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
        "AC959f452137bd815efcc433083914b75f",
        os.getenv("TWILIO_AUTH_TOKEN")
    )

