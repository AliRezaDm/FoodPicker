from django.db import models
from django.utils import html

# Manager
class CategoryQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='sub_category', null=True, blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50 , unique=True)
    status = models.BooleanField(default=True)

    # initializing the manager
    objects = CategoryQuerySet.as_manager()


    def __str__(self):
         return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']



class Ingredients(models.Model):
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.ForeignKey(Category, related_name="ingredients_category", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='media/ingredients/')
  
    def __str__(self):
         return self.name
    
    def thumbnail_tag(self):
        if self.thumbnail:
            return html.format_html("<img width=100; height=100, style='border-radius: 10px;' \
                                                       src='{}'>", self.thumbnail.url)
        return 'No Image'
    
    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        ordering = ['name']



class Recipe(models.Model):
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50 , unique=True)
    category = models.ManyToManyField(Category, related_name="food_category")
    ingredients = models.ManyToManyField(Ingredients, related_name="food_ingredients")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="media/recipe/")

    def __str__(self):
         return self.name
   
    def thumbnail_tag(self):
        if self.thumbnail:
            return html.format_html("<img width=100; height=100, style='border-radius: 10px;' \
                                                       src='{}'>", self.thumbnail.url)
        return 'No Image'
    
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['name']


class FoodImages(models.Model):
     
    recipe = models.ForeignKey(Recipe, related_name = 'gallary_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/recipe/gallary')
    order = models.PositiveBigIntegerField(default=0, unique=True)
    caption = models.CharField(max_length=100, blank=True, null=True)
     
    def __str__(self):
          return f'image for {self.recipe.name}'

    def thumbnail_tag(self):
        if self.image:
            return html.format_html("<img width=100; height=100, style='border-radius: 10px;' \
                                                       src='{}'>", self.image.url)
        return 'No Image'

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['order']
        
