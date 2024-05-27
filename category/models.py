from django.db import models
from sujal.models import CustomUser
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_icon = models.CharField(max_length=255)
    

    def __str__(self):
        return self.category_name

class CustomCategory(models.Model):
    category_name = models.CharField(max_length=255)
    category_icon = models.CharField(max_length=255)
    user = models.ForeignKey('sujal.CustomUser', on_delete=models.CASCADE)