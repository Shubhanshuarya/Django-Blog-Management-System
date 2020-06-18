from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post


def home_page(request):
    post_list = Post.objects.filter(status="published", editors_pick="yes")
    trending_post_list = Post.objects.filter(status="published", trending="yes")
    return render(request, 'blog/index.html', {'post_list': post_list, 'trending_post_list': trending_post_list})


def all_post_view(request):
    post_list = Post.objects.filter(status="published")
    return render(request, 'blog/categories.html', {'post_list': post_list})


def single_post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'blog/blog-single.html', {'post': post})


def contact_form(request):
    return render(request, 'blog/contact.html')
