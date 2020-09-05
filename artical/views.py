from django.shortcuts import render,reverse
from .forms import HeadForm,ContentsForm,Artical_f,comments_F,Category_Form
from django.shortcuts import redirect,HttpResponseRedirect
from .models import Head,Artical_m,comments,Category
from django.http import Http404,HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import models
from django.views.generic import DetailView,ListView,FormView

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

def show_articals(request):
    articals = Artical_m.objects.filter(status=1).all()
    #else:
        #articals = Artical_m.objects.filter(status=1).all()
        #articals_p = Artical_m.objects.filter(creater=request.user).all()
        #articals_p = Artical_m.objects.filter(creater= request.user)
        #articals = [ artical  for artical in articals_p if artical.creater== request.user]
        #articals.extend(articals_p)
    return render(request , 'show_content.html',{'articals':articals})


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
            new_artical.creater=request.user
            new_artical.save()
            return redirect('show_articals')
    context = {'form': form}
    return render(request,'create_artical.html',context)


@login_required
def delete_artical(request,artical_id):

    post= Artical_m.objects.get(id=artical_id)
    owner_topic_matcher(post,request.user)
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


# comments ------>>>>
@login_required
def comments_V(request,id):
    artical= Artical_m(id=id)
    #if request.method!="POST":
     #   form = comments_F()
    form = comments_F(request.POST)

    if form.is_valid():
        new_comment = form.save(commit=False)
        parent_to = request.POST.get('parent_to')
        if parent_to:
            new_comment.parent_to = comments.objects.get(id=parent_to)
        new_comment.comment_to = artical
        new_comment.commenter = request.user
        new_comment.save()
        print(new_comment.parent_to)
        return redirect('/artical_m/'+str(id))
    #context={"form":form,'artical':artical}
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


def artical_in(request,id):
    artical_m = Artical_m.objects.get(id=id)
    comment = comments.objects.filter(comment_to=artical_m).all()
    context = {'artical_m': artical_m,'comment':comment}
    return render(request, 'artical_in.html', context)


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


