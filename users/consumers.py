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
        print("in class connect")
        print(self.scope['session'])
        if self.scope['path']=='/ws/notifications/':
            self.room_group_name='%s' % self.scope['user']
            self.Susername=self.scope['user']
        else:
            self.Susername=self.scope['url_route']['kwargs']['Susername']
            self.Rusername=self.scope['url_route']['kwargs']['Rusername']
            self.room_group_name='group_name_%s' % self.create_group_name()
        print("group created "+self.room_group_name)
        async_to_sync(self.channel_layer.group_add)(self.room_group_name,self.channel_name)
        self.userStatus=1
        self.updateUserSession()
        #here add code inform user is online
        self.accept()


    def create_group_name(self):

        group_sort=sorted([check_name(self.Susername),check_name(self.Rusername)])
        name=''.join(group_sort)
        return name


    def disconnect(self, code):
        print("inside class dis")
        self.userStatus = 0
        self.updateUserSession()
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name,self.channel_name)


    def receive(self, text_data):
        print("inside class receive")
        text=save_chat(text_data)
        print("channel layer name - "+str(self.channel_layer))
        async_to_sync(self.channel_layer.group_send)(self.room_group_name,{
            'type':'chat_massage',
            'massage':text,
            'send_time':str(datetime.now().isoformat()),
            'sender':self.Susername,
        })
        async_to_sync(self.channel_layer.group_send)(self.Rusername, {
            'type': 'notification_massage',
            'massage': text,
            'send_time': str(datetime.now().isoformat()),
            'sender': self.Susername,
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

    def notification_massage(self,event):
        print(event)
        self.send(text_data=json.dumps({'massage':event}))

def check_name(strin):
    return strin.split('@')[0]



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

class UserNotification(WebsocketConsumer):
    def connect(self):
        user=self.scope['url_route']['kwargs']['user']



