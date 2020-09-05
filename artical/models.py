from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render,reverse

Status = ((1,'posted'),(0,'in_progress'))
# Create your models here.
class Head(models.Model):
    txt = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    #auther = models.
    def __str__(self):
        return self.txt


class Contents(models.Model):
    header = models.ForeignKey(Head,on_delete=models.CASCADE,null=True)
    txt = models.TextField()
    content_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'contente'
    def __str__(self):
        return f"{self.txt[:50]}..."


class Artical_m(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    #it will be called when instance is created auto_add_now but when
    # every time save is called add now called
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True,null=True)
    said = models.TextField()
    likes = models.ManyToManyField(User,related_name='blog_likes')
    creater = models.ForeignKey(User,on_delete= models.CASCADE,null=True)
    status = models.IntegerField(choices=Status, default=0)
    categories = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True)
    In_image = models.ImageField(blank=True)
    class Meta:
        ordering = ['-create_date']
    def __str__(self):
        return self.said


class Profile(models.Model):
    creater = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    bio = models.CharField(max_length=400)
    profile_image = models.ImageField(blank=True)
    #twitter_link = blog = models.CharField(max_length=250,null=True,blank=True)
    instagram = models.CharField(max_length=250,null=True,blank=True)
    facebook = models.CharField(max_length=250,null=True,blank=True)
    website_link = models.CharField(max_length=250,null=True,blank=True)
    def __str__(self):
        return str(self.creater)


class comments(models.Model):
    comment_to = models.ForeignKey(Artical_m,
                on_delete=models.CASCADE)

    text=models.TextField()
    commenter=models.ForeignKey(User,
                on_delete=models.CASCADE)
    name = models.CharField(max_length=67,null=True,blank=True)
    parent_to=models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.text)
    def childrens(self):
        return comments.objects.filter(parent_to=self)
    def get_abslute_url(self):
        return reverse(self)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,max_length=40)
    parent_to = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    class Meta:
        unique_together =('parent_to','slug')
    def __str__(self):
        full_path = [self.name]
        prt=self.parent_to
        while prt is not None:
            full_path.append(prt.name)
            prt=prt.parent_to
        return '->'.join(full_path[::-1])








