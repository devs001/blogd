from django.db import models
from django.contrib.auth.models import User

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
    creater = models.ForeignKey(User,on_delete= models.CASCADE,null=True)
    status = models.IntegerField(choices=Status, default=0)
    In_image = models.ImageField(blank=True)
    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.said

class profile(models.Model):
    creater = models.OneToOneField(User,null=True,no_delete=models.CASCADE)
    blog = models.Charfield(max_legth)









