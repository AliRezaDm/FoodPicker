from django.db import models
from django.utils import html
from django.utils.text import slugify
from .utils import ThumbnailMixin
from django_countries.fields import CountryField

class BaseModel(models.Model):
    """ a base model contianing slug to make sure same field does not get repeated in each model """
    slug = models.SlugField(max_length=50, unique=True)
    # to create slug automatically 
    def save(self, *args, **kwargs):
        # checks if the model has a field called name, then create the slug based on name field
        if not self.slug and hasattr(self, 'name'):
            self.slug = slugify(self.name)
        return super().save(**args, **kwargs)
    
    class Meta:
        abstract = True


# Manager
class CategoryQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=True)


class Category(BaseModel):

    Ingredients = 'I'
    Recipe = 'R'
    TYPE_CHOICES = ((Ingredients, 'Ingredients'), 
                    (Recipe, 'Recipe'))

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='sub_category', null=True, blank=True)
    name = models.CharField(max_length=100)
    type =  models.CharField(max_length=2, choices=TYPE_CHOICES)
    status = models.BooleanField(default=True)

    # initializing the manager
    objects = CategoryQuerySet.as_manager()


    def __str__(self):
         return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']



class Ingredients(BaseModel, ThumbnailMixin):
    
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="ingredients_category", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='media/ingredients/')
  
    def __str__(self):
         return self.name
    

    
    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        ordering = ['name']



class Recipe(BaseModel, ThumbnailMixin):

    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS_CHOICES = [(DRAFT, 'Draft'), 
                      (PUBLISHED, 'Published')]
    
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, related_name="food_category")
    ingredients = models.ManyToManyField(Ingredients, related_name="food_ingredients")
    country = CountryField(blank=True)  
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="media/recipe/")
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
         return self.name
    
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['name']


class FoodImages(models.Model, ThumbnailMixin):
     
    recipe = models.ForeignKey(Recipe, related_name = 'gallary_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/recipe/gallary')
    # to set the order of image display manually 
    order = models.PositiveBigIntegerField(default=0, unique=True)
    # optional caption for each image 
    caption = models.CharField(max_length=100, blank=True, null=True)
     
    def __str__(self):
          return f'image for {self.recipe.name}'

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['order']
        
