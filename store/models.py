from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug =models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural= 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    user = models.ForeignKey(User, related_name='products',on_delete=models.CASCADE)
    category=models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug =models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    author = models.SlugField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    edition = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
