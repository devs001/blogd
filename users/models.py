from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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


    def relation(self):
        return [self.sender,self.receiver]


