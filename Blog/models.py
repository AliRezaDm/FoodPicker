from django.db import models
from django.utils.text import slugify
from Food.utils import ThumbnailMixin



# Manager
class CategoryQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=True)

class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=50)
    status = models.BooleanField(default=True)

    # initializing the manager
    objects = CategoryQuerySet.as_manager()
  
    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(**args, **kwargs)
    
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


    # initializing the manager
    objects = CategoryQuerySet.as_manager()


class Article(models.Model, ThumbnailMixin):

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50)
    category = models.ForeignKey(Category, related_name='article_category', on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default = True)
    thumbnail = models.ImageField(upload_to='media/blog/')   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    # handling creating slug in the model instead of API 
    # it get created automatically across the app not just in the API
    def save(self, *args, **kwargs):
        #checks if there is no slug creates one
        if not self.slug:
            self.slug = slugify(self.title)    
        super().save(*args, **kwargs)



    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ["created"]
