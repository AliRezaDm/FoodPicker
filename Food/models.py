from django.db import models

class Category(models.Model):
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50 , unique=True)
    status = models.BooleanField(default=True)

    def __str__(self):
         return self.title



class Ingridients(models.Model):
    
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="ingridients_category", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='media/ingridients/')
  
    def __str__(self):
         return self.name


class Reciepe(models.Model):
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50 , unique=True)
    category = models.ManyToManyField(Category, related_name="food_category")
    description = models.TextField()
    ingridients = models.ManyToManyField(Ingridients, related_name="food_ingridients")
    thumbnail = models.ImageField(upload_to="media/reciepe/")

    def __str__(self):
         return self.name
    

class FoodImages(models.Model):
     
     reciepe = models.ForeignKey(Reciepe, related_name = "reciepe_images", on_delete=models.CASCADE)
     image = models.ImageField(upload_to='media/reciepe/')
     
     def __str__(self):
          return self.reciepe.name 




