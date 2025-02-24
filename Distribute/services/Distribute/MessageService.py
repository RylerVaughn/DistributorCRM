from twilio.rest import Client

# High level function used specifically for django views. Made for decoding message templates and routing it to all clients provided.
def SendTextMessages(client_list: list, message_template: str):
    
    # Create internal function for decoding message templates here.

    print('hello')


SendTextMessages([], 'hukfosjiof')


