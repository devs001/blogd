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
        model = Contents
        fields = ['txt']
        lebals = {'txt': 'contents:'}

class Artical_f(forms.ModelForm):
    class Meta:
        model = Artical_m
        fields = ['title','slug','said'
                  ,'status','In_image','categories']

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

