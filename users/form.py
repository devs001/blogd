from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    url=forms.URLField()
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    class Meta:
        model= User
        fields = ('username','first_name','last_name',
                  'password1','password2','email')
    """def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__()
        #self.fields=[]"""

class Profile_f(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio','profile_image','instagram','website_link')