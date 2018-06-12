import image as image
from django.db import models
from django.db.models import permalink

# Create your models here.
import blog


class Category(object):
    pass


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField()
    id(Category)==id


class Blog(object):
    pass


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    #image = models.ImageField()
    slug = models.SlugField()
    description = models.TextField()
    blog = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    id(Blog)==id
    #author

    def __unicode__(self):
        return '%s' % self.title

    def snippet(self):
        return self.Blog.blog[:50]

    '''@permalink
    def get_absolute_url(self):
        return 'view_categories', None, {'slug': self.slug}'''

def __str__(self):
    return self.title

