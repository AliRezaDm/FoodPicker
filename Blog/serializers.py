from django.utils.text import slugify
from rest_framework import serializers

from .models import Category, Article


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['slug', 'status']

    
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['created_at', 'update_at', 'slug', 'status']
