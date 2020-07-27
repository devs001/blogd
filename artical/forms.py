from django import forms
from .models import Head,Contents,Artical_m
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
                  ,'status','In_image']
