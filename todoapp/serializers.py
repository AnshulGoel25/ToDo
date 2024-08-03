from rest_framework import serializers
from .models import Todo, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed', 'created', 'category']