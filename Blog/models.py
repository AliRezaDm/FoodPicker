from django.db import models
from django.utils import html 


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
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


    # initializing the manager
    objects = CategoryQuerySet.as_manager()


class Article(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50)
    category = models.ForeignKey(Category, related_name='article_category', on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default = True)
    thumbnail = models.ImageField(upload_to='media/blog/')   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def thumbnail_tag(self):
        #checks for the existence of thumbnail before hand
        if self.thumbnail:
            return html.format_html("<img width=100; height=100, style='border-radius: 10px;' \
                                                    src='{}'>", self.thumbnail.url)
        return 'No Image'
    

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ["created"]
