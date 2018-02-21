from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    context = {
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html', context)

def post_add(request):

    if request.method == 'POST':


        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(
            author = request.user,
            title = title,
            content = content,
        )


        return redirect('post-detail', pk=post.pk)
    else:
        return render(request, 'blog/post_add.html')

def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
    return redirect('post-list')
