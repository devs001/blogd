from django.db import models
from django.contrib.auth.models import User
#from allauth.socialaccount.models import SocialAccount
# Create your models here.
from allauth.account.adapter import DefaultAccountAdapter
#class adapter(DefaultAccountAdapter):
 #   def save_user(self, request, user, form, commit=True):


Online='online'
Offline='offline'
Status =((1,'onLine'),(0,'offLine'))

class Profile(models.Model):
    creater = models.OneToOneField(User,on_delete=models.CASCADE,null=True,related_name='profile_to')
    bio = models.TextField(max_length=500)
    profile_image = models.ImageField(blank=True)
    #twitter_link = blog = models.CharField(max_length=250,null=True,blank=True)
    instagram = models.URLField(max_length=250,null=True,blank=True)
    facebook = models.URLField(max_length=250,null=True,blank=True)
    website_link = models.URLField(max_length=250,null=True,blank=True)
    def __str__(self):
        return str(self.creater)



class ChatRel(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    chatText=models.CharField(max_length=1000)
    send_time=models.DateTimeField(auto_now_add=True)
    receive_time=models.DateTimeField(null=True,blank=True)
    class Meta:
        ordering = ['-send_time']

    def __str__(self):
        return str(self.chatText)

    def last_chat(self):
        last=ChatRel.objects.filter(sender=self.sender,receiver=self.receiver)[-1]
        print("-----"+str(len(last)))
        if last:
            return last.chatText
        else:
            return "no massage yet start a conversation"


    def relation(self):
        return [self.sender,self.receiver]


class UserLastSession(models.Model):
    status=models.IntegerField(choices=Status,default=0)
    lastLogin=models.DateTimeField(auto_now=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='last_online_info')

    def __str__(self):
        return str(self.user)

