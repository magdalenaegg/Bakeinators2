from django.db import models


# Create your models here.


class Category(object):
    pass


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField()
    id(Category)==id
    def __unicode__(self):
        return '%s' % self.title

class Blog(object):
    pass


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    item_photo = models.ImageField(default='default.png', upload_to='media')
    slug = models.SlugField()
    description = models.TextField()
    ingredients = models.TextField(list)
    blog = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    id(Blog)==id
    #author

    def __unicode__(self):
        return '%s' % self.title


    '''@permalink
    def get_absolute_url(self):
        return 'view_categories', None, {'slug': self.slug}'''

def __unicode__(self):
    return self.title

