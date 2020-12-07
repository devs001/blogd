from django.shortcuts import render,reverse
from .forms import HeadForm,ContentsForm,Artical_f,comments_F,Category_Form,Email_Share
from django.shortcuts import redirect,HttpResponseRedirect,get_object_or_404
from .models import Head,Artical_m,comments,Category,TaggableManager
from taggit.models import Tag
from django.http import Http404,HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
import json
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import models
from django.views.generic import DetailView,ListView,FormView
from django.core.mail import send_mail,EmailMessage

def first(request):
    return render(request,'base.html')


def heade(request,id):

    return render(request, 'base.html',{'id':id})


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

def show_articals(request):
    articals = Artical_m.posted.all()
    #else:
        #articals = Artical_m.objects.filter(status=1).all()
        #articals_p = Artical_m.objects.filter(creater=request.user).all()
        #articals_p = Artical_m.objects.filter(creater= request.user)
        #articals = [ artical  for artical in articals_p if artical.creater== request.user]
        #articals.extend(articals_p)
    return render(request , 'show_content.html',{'articals':articals})
@login_required
def Dashbroad(request):
    articals = Artical_m.objects.all().filter(creater=request.user)

    #else:
        #articals = Artical_m.objects.filter(status=1).all()
        #articals_p = Artical_m.objects.filter(creater=request.user).all()
        #articals_p = Artical_m.objects.filter(creater= request.user)
        #articals = [ artical  for artical in articals_p if artical.creater== request.user]
        #articals.extend(articals_p)
    return render(request , 'dashboard.html',{'articals':articals})

@login_required
def show_drafts(request):
    articals = Artical_m.objects.filter(status=0).filter(creater=request.user).all()
    # else:
    # articals = Artical_m.objects.filter(status=1).all()
    # articals_p = Artical_m.objects.filter(creater=request.user).all()
    # articals_p = Artical_m.objects.filter(creater= request.user)
    # articals = [ artical  for artical in articals_p if artical.creater== request.user]
    # articals.extend(articals_p)
    return render(request, 'show_drafts.html', {'articals': articals})


@login_required
def create_artical(request):
    if request.method != 'POST':
        form = Artical_f()
    else:
        form = Artical_f(request.POST,request.FILES)
        if form.is_valid():
            new_artical=form.save(commit=False)
            new_artical.creater = request.user
            new_artical.save()
            form.save_m2m()
            return redirect('show_articals')
    context = {'form': form}
    return render(request,'create_artical.html',context)


@login_required
def delete_artical(request,artical_slug):
    post= Artical_m.objects.get(id=artical_slug)
    owner_topic_matcher(post,request.user)
    post.delete()
    return redirect('show_articals')

@login_required
def edits_artical(request,slug):
    artica=Artical_m.objects.get(slug=slug)
    owner_topic_matcher(artica,request.user)
    if request.method !='POST':
        form=Artical_f(instance=artica)
    else:
        form=Artical_f(request.POST,request.FILES,instance=artica)
        if form.is_valid():
            edited_artical=form.save(commit=False)
            edited_artical.creater = request.user
            edited_artical.save()
            return redirect(artica.get_absolute_url())
    context = {'form':form,'artica':artica}
    return render(request,'edit_content.html',context)
def owner_topic_matcher(topic,user):
    if topic.creater != user:
        raise Http404


# comments ------>>>>
#@login_required
def comments_V(request,id):
    print("commante here")
    artical= Artical_m(id=id)
        #form.text=request.POST.get('comment_text')
        #print(form.text)
    if request.method=='POST':
        form = comments_F(request.POST or None)
        if form.is_valid():
            print("its valid form")
            #if request.is_ajax:
             #   form.text = request.POST.get('comment_text')
            new_comment = form.save(commit=False)
            parent_to = request.POST.get('parent_to')
            if parent_to:
                new_comment.parent_to = comments.objects.get(id=parent_to)
            new_comment.comment_to = artical
            new_comment.commenter = request.user
            new_comment.save()
            print(new_comment.parent_to)
            #return redirect('/artical_m/'+str(id))
            context={"form":form,'artical':artical}
            if request.is_ajax:
                comment = comments.objects.filter(comment_to=artical).all()
                context={"comment":comment}
                html=render_to_string('comments.html',context,request=request)
                return JsonResponse({'form':html})
        else:
            print("its valid not form")
            return HttpResponse(" its not working")


class CommentsList(ListView):
    template_name = 'artical_in.html'
    model = comments
    context_object_name = "comments"
    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        val = self.kwargs['id']
        print(str(val)+"----------------------------------------------"
                       "----------------------------------------------")
        artical=Artical_m.objects.get(id=val)
        # filter by a variable captured from url, for example
        return qs.filter(comment_to=artical,)


def artical_in(request,slug):
    artical_m = Artical_m.objects.get(slug=slug)
    articals = Artical_m.objects.all()
    tags=artical_m.tags.all()
    comment = comments.objects.filter(comment_to=artical_m).all()
    like_status=False
    if request.user.is_authenticated:
        if  artical_m.likes.filter(id=request.user.id):
            like_status=True
    context = {'artical_m': artical_m,'comment':comment,'articals':articals,'tags':tags,'like_status':like_status}
    return render(request, 'artical_in.html', context)
def liked(request):
    id=1
    print("lol1")
    if not request.user.is_authenticated:
        like="login requied"
        ctx = {"like": like}
        return HttpResponse(json.dumps(ctx), content_type='application/json')
    if request.method=="POST":
        print("lol")
        if request.POST.get("operation")== "likeop" and request.is_ajax():
            jax_id=request.POST.get("jax_id")
            artical_m=Artical_m.objects.get(id=jax_id)
            if artical_m.likes.filter(id=request.user.id):
                like=False
                artical_m.likes.remove(request.user)
            else:
                like=True
                artical_m.likes.add(request.user)
            artical_m.save()
            ctx = { "like": like}
            return HttpResponse(json.dumps(ctx), content_type='application/json')
    artical_m = Artical_m.objects.get(id=id)
    print(request.user)
    #we are not using form so we have to user add() method
    if artical_m.likes.filter(id=request.user.id):
        artical_m.likes.remove(request.user)
    else:
        artical_m.likes.add(request.user)
    artical_m.save()
    return redirect(artical_m.get_absolute_url())




class Category_add(FormView):
    template_name = 'categoryadd.html'
    form_class = Category_Form
    success_url = 'create_artical'
    def get_context_data(self, **kwargs):
        context = super(Category_add,self).get_context_data(**kwargs)
        cato = Category.objects.all()
        form=self.form_class
        context={'categorys':cato,'form':form}
        return context
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('create_artical')

#--------> search <-------
class Search(ListView):
    template_name = 'serach_result.html'
    context_object_name = 'result'
    model= Artical_m
    def get_queryset(self):
        rs = super().get_queryset()
        qu=self.request.GET.get('st')
        rs=self.model.posted.all().filter(Q(title__contains=qu))
        return rs


class tags(ListView):
    template_name = 'tagsh.html'
    context_object_name = 'result'
    model= Artical_m
    def get_queryset(self):
        rs = super().get_queryset()
        qu=self.kwargs['slug']
        tagO=get_object_or_404(Tag,slug=qu)
        rs=self.model.objects.filter(tags=tagO)
        print(rs)
        return rs

def Email_Share_V(request,id):
    artical=Artical_m.objects.get(id=id)
    send=False
    if request.method !='POST':
        form=Email_Share()
    else:
        form=Email_Share(request.POST)
        if form.is_valid():
            # share ....
            artical_url= request.build_absolute_uri(artical.get_absolute_url())
            data=form.cleaned_data
            subject = f"{data['Email']} recommends you read " f"{artical.title}"
            massage = f"Read {artical.title} at {artical_url} \n\n " f"{data['Comments']}"
            send_mail(subject=subject,message=massage,from_email='devendersandhu001@gmail.com',
                      recipient_list=[data['To']],fail_silently=False)
            send =True
    context={'form':form,'artical':artical,"send":send}
    return render(request,'share_email.html',context)
