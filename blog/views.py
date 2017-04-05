from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import Post

# Create your views here.


def post_list(request):

    post_list = Post.objects.all()
    search = request.GET.get('search')

    if search:
        post_list = post_list.filter(text__icontains=search)

    return render_to_response('blog/post_list.html', {'post_list': post_list, 'search': search})


def post_view(request, pk):

    post = Post.objects.get(id=pk)

    return render_to_response('blog/post_view.html', {'post': post})


def test(request):

    name = request.user
    html = "<p>Hi, {}! Welcome to the custom page.</p".format(name)

    return HttpResponse(html)
