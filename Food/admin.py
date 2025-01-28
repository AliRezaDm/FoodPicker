from django.contrib import admin
from .models import *

#inline for Recipe
class FoogImageInLine(admin.TabularInline):
    model = FoodImages
    extra = 1 
    fields = ['image', 'caption','order']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['title', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug':('title',)}


@admin.register(Ingredients)
class Ingredients(admin.ModelAdmin):

    list_display = ['name', 'category_name', 'thumbnail_tag']
    readonly_fields = ('thumbnail_tag',)
    search_fields = ['name']
    prepopulated_fields = {'slug':('name',)}

    # to display category name
    def category_name(self, obj):
        return obj.category.name
    category_name.short_description = 'Category'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ['name', 'get_category', 'get_ingredients', 'thumbnail_tag']
    readonly_fields = ('thumbnail_tag',)
    search_fields = ['name', 'ingredients__name']
    prepopulated_fields = {'slug':('name',)}
    inlines = [FoogImageInLine]

    def get_category(self, obj):
        return " - ".join([category.title for category in obj.category.active()])
    get_category.short_description = 'Categories'

    def get_ingredients(self, obj):
        return ", ".join([ingredient.name for ingredient in obj.ingredients.all()])
    get_ingredients.short_description = 'Ingredients' 


@admin.register(FoodImages)
class FoodImagesAdmin(admin.ModelAdmin):

    list_display = ['recipe','image', 'caption', 'order']
    search_fields = ['recipe__name']
    list_editable = ['order']
