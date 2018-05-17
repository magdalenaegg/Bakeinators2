from django.shortcuts import render_to_response, get_object_or_404


# Create your views here.
from blog.models import Category, Blog


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, id):
    category = None

    try:
        category = Category.objects.get(id=id)
    except:
        pass

    posts = Blog.objects.filter(category=category)[:5]


    return render_to_response('view_category.html', {
        'category': category,
        'posts': posts
    })