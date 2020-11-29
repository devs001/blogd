from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .form import SignUpForm,Profile_f
# Create your views here.
def register(request):
    if request.method != 'POST':
        form = SignUpForm()
        Eform = Profile_f()
    else:
        form = SignUpForm(data=request.POST)
        Eform = Profile_f(request.POST,request.FILES)
        if form.is_valid() and Eform.is_valid():
            new_user=form.save()
            new_userE=Eform.save(commit=False)
            new_userE.creater=new_user
            new_userE.save()
            login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('show_articals')
    context = {'form': form,'Eform': Eform}
    return render(request, 'register_t.html', context)

