from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import OuterRef, Count, Exists

from .forms import LikeForm, PostForm
from .models import Like, Post

def hello(request: HttpRequest) -> HttpResponse:
    # return HttpResponse('Hello World')
    return render(request, 'webapp/hello.html')

@login_required(login_url='/admin/login/')
def index(request: HttpRequest) -> HttpResponse:
    # posts = Post.objects.all()
    # posts = Post.objects.filter(user=request.user)

    # Verificar se o usuário curtiu o post (SubQuery)
    user_like = Like.objects.filter(
        user=request.user, 
        post=OuterRef('id'))
    
    posts = Post.objects.prefetch_related('like_post').annotate(
        count_likes=Count('like_post'), 
        user_liked=Exists(user_like))
    
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = request.user
            form_save.save()
            # return HttpResponse('Foto salva')
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'webapp/index.html', { 'form': form, 'posts': posts })

@login_required(login_url='/admin/login/')
def like(request: HttpRequest) -> HttpResponseRedirect:
    if request.method=='POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            # form_save = form.save(commit=False)
            # form_save.user = request.user
            # form_save.save()
            check_like = Like.objects.filter(post=form.cleaned_data['post'], user=request.user).exists()
            if check_like:
                Like.objects.filter(post=form.cleaned_data['post'], user=request.user).delete()
            else:
                form_save = form.save(commit=False)
                form_save.user = request.user
                form_save.save()
    return redirect('/')
