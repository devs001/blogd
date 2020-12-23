from django.shortcuts import render,redirect,reverse,resolve_url,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .form import SignUpForm,Profile_f,ChatForm
from django.contrib.auth.models import User
from .models import ChatRel
from django.db.models import Q
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


def ChatRoom(request,receiver_username):
    if request.method != 'POST':
        users=User.objects.all()

        Receiver=User.objects.get(username=receiver_username)
        print()
        print("----------")
        chats= ChatRel.objects.filter(Q(sender=request.user.id , receiver = Receiver.id ))
        chatR = ChatRel.objects.filter(Q(sender=Receiver.id, receiver=request.user.id))
        print("ppppp")
        print(chatR)
        print("ppppp")
        chate=(chats | chatR).order_by('send_time')
        print(chate)
        form = ChatForm()
    else:
        form = ChatForm(request.POST)
        if form.is_valid():
            new_chat=form.save(commit=False)
            new_chat.sender = request.user
            new_chat.receiver=User.objects.get(username=receiver_username)
            new_chat.save()
            form.save_m2m()
            print(receiver_username+" <----")
            return HttpResponseRedirect(receiver_username)
    context = {'form': form,'chats':chate,'receiver_username':receiver_username,'users':users,'receiver':Receiver}
    return render(request,'chatroom.html',context)
    
