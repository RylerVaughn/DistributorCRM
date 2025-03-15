
# Made to simply carry text message information, reducing complexity.

class TextMessage():
    def __init__(self, sender: str, reciever: str, body: str):
        self.sender = sender
        self.reciever = reciever
        self.body = body

    def __str__(self):
        return f"{self.sender}: {self.body}"