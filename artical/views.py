from django.shortcuts import render
from .forms import HeadForm,ContentsForm,Artical_f
from django.shortcuts import redirect
from .models import Head,Artical_m
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import models


def first(request):
    return render(request,'base.html')


def heade(request):
    return render(request, 'base.html')


def create_head(request):
    form = HeadForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('show_headin')


def show_heading(request):
    pp = Head.objects.order_by('date_added')
    context = {'pp': pp}
    return render(request, 'show_header.html', context)


@login_required
def create_contents(request, head_id):
    #extrating header for both time to use
    header = Head.objects.get(id=head_id)
    if request.method != 'POST':
        form = ContentsForm()
    else:
        form = ContentsForm(data=request.POST)
        if form.is_valid():
            contents = form.save(commit=False)
            contents.header = header
            contents.save()
            return redirect('show_contents', head_id=head_id)
    context = {'form': form, 'header': header}
    return render(request,'create_content.html', context)


def show_contents(request, head_id):
    heado = Head.objects.get(id=head_id)
    contente = heado.contents_set.all()
    print('number of'+str(len(contente)))
    print(contente)
    context = {'heado': heado,'contente': contente}
    return render(request, 'show_content.html', context)


@login_required
def show_articals(request):
    articals_c = Artical_m.objects.filter(status=1).all()
    articals_p = Artical_m.objects.filter(creater=request.user).all()
    articals = [ artical  for artical in articals_p if artical.creater== request.user]
    articals.extend(articals_c)
    return render(request , 'show_content.html',{'articals':articals})


@login_required
def create_artical(request):
    if request.method != 'POST':
        form = Artical_f()
    else:
        form = Artical_f(request.POST,request.FILES)
        if form.is_valid():
            new_artical=form.save(commit=False)
            new_artical.creater=request.user
            new_artical.save()
            return redirect('show_articals')
    context = {'form': form}
    return render(request,'create_artical.html',context)

def delete_artical(request,artical_id):
    post= Artical_m.objects.get(id=artical_id)
    post.delete()
    return redirect('heade')


def edits_artical(request,articals_id):
    artica=Artical_m.objects.get(id=articals_id)
    if request.method !='POST':
        form=Artical_f(instance=artica)
    else:
        form=Artical_f(request.POST,request.FILES,instance=artica)
        if form.is_valid():
            edited_artical=form.save(commit=False)
            edited_artical.creater = request.user
            edited_artical.save()
            return redirect('heade')
    context = {'form':form,'artica':artica}
    return render(request,'edit_content.html',context)
def owner_topic_matcher(topic,user):
    if topic.creater != user:
        raise Http404