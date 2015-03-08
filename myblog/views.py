from django.shortcuts import render,RequestContext,HttpResponse,render_to_response,redirect,HttpResponseRedirect,get_object_or_404
from models import *
from forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    
        posts = Post.objects.all().order_by("createDate")
        return render_to_response('index.html', {
            'posts': posts
            }, RequestContext(request))
    



def newpost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
    return render_to_response('form.html', {
        'form': form
    }, RequestContext(request))



def detailpost(request, pk):
    post = get_object_or_404(Post, id=pk)

    return render_to_response('details.html', {
        'post': post
    }, RequestContext(request))



def deletepost(request, pk):
    Post.objects.filter(id=pk).delete()

    return redirect(reverse('home'))


def editpost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    return render_to_response('edit.html', {
        'form': form,
        'post': post
    }, RequestContext(request))
	
def newcomment(request, pk):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.instance.post = Post.objects.get(id=pk)
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render_to_response('detail.html', {}, RequestContext(request))
def deletecomment(request, pk):
    Comment.objects.get(id=pk).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))