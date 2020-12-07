import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from .models import ChatRel

def print_show():
    print(" its working here")

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print("inside class connect")
        self.accept()

    def disconnect(self, code):
        print("inside class dis")
        pass

    def receive(self, text_data):
        print("inside class recive")
        text=save_chat(text_data)
        self.send(text_data=json.dumps({'massage':text}))

def save_chat(data):
    textDataJson = json.loads(data)
    massageback = textDataJson['chatText']
    receiver_username = textDataJson['receiver_username']
    sender_username = textDataJson['sender_username']
    receiver=User.objects.get(username=receiver_username)
    sender=User.objects.get(username=sender_username)
    new_chat= ChatRel.objects.create(chatText=massageback,receiver=receiver,sender=sender)
    new_chat.save()
    return massageback


