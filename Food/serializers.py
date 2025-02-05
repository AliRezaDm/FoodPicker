from rest_framework import serializers

from .models import Category, Ingredients, Recipe, FoodImages

class CategorySerializer(serializers.ModelSerializer):

    # to list subcategories(children of this category)
    sub_category = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = Category
        # both parent and children to the category are shown
        fields = ['parent', 'name', 'slug', 'status', 'type', 'sub_category']
        read_only_fields = ('slug', 'status')


class IngredientsSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Ingredients
        fields = ['id', 'name', 'category', 'thumbnail']

class RecipeSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True, many=True)
    ingredients = IngredientsSerializer(read_only=True, many=True)
    #bringing related image to the Recipe from the image gallary
    gallary_image = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'slug', 'category', 'ingredients', 'country', 'description', \
                                                    'thumbnail', 'gallary_image', 'status']
        read_only_fields = ('status', 'slug')

class FoodImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodImages
        fields = '__all__'
