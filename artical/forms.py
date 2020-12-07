from tinymce.widgets import TinyMCE
from django import forms
from .models import (Head,Contents,Artical_m,comments,Category)
from django.contrib import admin


class HeadForm(forms.ModelForm):
    class Meta:
            model = Head
            #we include only header field from  model
            fields = ['txt']
            # to keep it empty not to use it we enter a empty string
            labels = {'txt': ''}


class ContentsForm(forms.ModelForm):
    class Meta:
        fields = ['txt']
        lebals = {'txt': 'contents:'}

class TinyMce(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class Artical_f(forms.ModelForm):
    said= forms.Textarea()
    content=forms.CharField(widget=TinyMCE(attrs={'required':False,"cols":30,'rows':10}))
    class Meta:
        model = Artical_m
        fields = ['title','slug','said'
                  ,'status','In_image','categories','tags','content']

class comments_F(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['text']
        lebals = {'text': ''}


class Category_Form(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name','slug','parent_to']
        lables = {'names': 'names','slug': 'slugs'}


class Email_Share(forms.Form):
    Email=forms.EmailField()
    To=forms.EmailField()
    Comments=forms.CharField(max_length=350,required=False)
