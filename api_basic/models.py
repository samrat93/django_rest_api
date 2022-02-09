from pyexpat import model
from django.db import models

# Create your models here.


class Article(models.Model):
    """Creating artical model for database"""

    title = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Return the title of artical model"""
        return self.title
