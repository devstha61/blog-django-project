from django.shortcuts import render

from blog_app.models import Post

def post_list(request):
    posts = Post.objects.filter(published_at__isnull=False)
    return render(
        request,
        "post_list.html",
        {"posts": posts},
    )

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        "post_detail.html",
        {"post": post},
    )