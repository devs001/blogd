import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from .models import ChatRel,UserLastSession
from datetime import datetime,timezone
from asgiref.sync import async_to_sync
def print_show():
    print(" its working here")

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print("inside class connect")
        self.Susername=self.scope['url_route']['kwargs']['Susername']
        self.Rusername=self.scope['url_route']['kwargs']['Rusername']
        #self.request=self.scope['url_route']['kwargs']['request']
        self.room_group_name='group_name_%s' % self.create_group_name()
        print("----------gggggg----"+self.room_group_name)
        async_to_sync(self.channel_layer.group_add)(self.room_group_name,self.channel_name)
        self.userStatus=1
        self.updateUserSession()
        #here add code inform user is online
        self.accept()

    def create_group_name(self):
        print()
        group_sort=sorted([self.Susername,self.Rusername])
        name=''.join(group_sort)
        return name

    def disconnect(self, code):
        print("inside class dis")
        self.userStatus = 0
        self.updateUserSession()
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name,self.channel_name)


    def receive(self, text_data):
        print("inside class recive")
        text=save_chat(text_data)
        print(self.channel_layer)
        print(self.room_group_name)
        async_to_sync(self.channel_layer.group_send)(self.room_group_name,{
            'type':'chat_massage',
            'massage':text,
            'send_time':str(datetime.now().isoformat()),
            'sender':self.Susername,
        })
        #self.send(text_data=json.dumps({'massage':text}))
    def updateUserSession(self):
        Sid=User.objects.get(username=self.Susername)
        user,created=UserLastSession.objects.get_or_create(user=Sid)
        print((datetime.now(timezone.utc)-user.lastLogin).seconds)
        user.status=self.userStatus
        user.save()
    def chat_massage(self,event):
        print(event)
        self.send(text_data=json.dumps({'massage':event}))


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


