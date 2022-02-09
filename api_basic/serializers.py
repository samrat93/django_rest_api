from dataclasses import field
import imp
from unittest.util import _MAX_LENGTH
from itsdangerous import Serializer
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """Using ModelSerializer"""
    class Meta:
        model = Article
        fields = ['id', 'title', 'auther','email','date']


''' Using serializer.Serializer

class ArticleSerializer(serializers.Serializer):
    """Creating artical serializer for api_basic app"""

    title = serializers.CharField(max_length=100)
    auther = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()
 

    def create(self, validated_data):
        """Creating create function for serializer"""

        return Article.objects.create(validated_data)


    def update(self, instance, validate_data):
        """Creating update function serializer"""

        instance.title = validate_data.get('title', instance.title)
        instance.author = validate_data.get('author', instance.author)
        instance.email = validate_data.get('email', instance.email)
        instance.date = validate_data.get('date', instance.date)
        instance.save()
        return instance

       '''
