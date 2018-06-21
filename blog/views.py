from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404



# Create your views here.
from .models import Category, Blog



def index(request):
 return render_to_response('index.html', {
     'categories': Category.objects.all(),
     'posts': Blog.objects.all()
 })

def view_post(request, id):
   posts = Blog.objects.filter(id=id)
   post = Blog.objects.get(pk=id)
   return render_to_response('view_post.html', {
        'post': post, 'posts': posts
    })

def view_posts(request):
    posts = Blog.objects.all().order_by('posted')

#    except:
 #       pass

    return render_to_response('view_posts.html', {
        'posts': posts,
      })

def view_category(request, id):
    category = None

    try:
        category = Category.objects.get(id=id)
    except:
        pass

    posts = Blog.objects.filter(category=category)[:15]


    return render_to_response('view_category.html', {
        'category': category,
        'posts': posts
    })

def view_categories(request):
    try:
        categories = Category.objects.all()
    except:
        pass

    return render_to_response('view_categories.html', {
      'categories': categories.all(),
      })

#def blog(request):
