from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def index(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', post_id)
        
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update.html', {'form': form})

def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('index')