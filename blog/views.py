from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render


# Create your views here.
from blog.models import Category, Blog


def index(request):
 return render_to_response('index.html', {
     'categories': Category.objects.all(),
     'posts': Blog.objects.all()[:15]
 })

def view_post(request, slug):
    #posts = Blog.objects.all()
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_posts(request):
    try:
        posts = Blog.objects.all()
    except:
        pass

    return render_to_response('view_posts.html', {
        'post': posts,
      })

def view_category(request, slug):
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

def view_categories(request):
    categories = []

    try:
        categories = Category.objects.all()
    except:
        pass

    return render_to_response('view_categories.html', {
        'categories': categories,
      })

#def blog(request):
