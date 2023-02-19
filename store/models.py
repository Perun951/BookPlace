from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,default='')
    class Meta:
        verbose_name_plural= 'Categories'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Product(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETED = 'deleted'

    STATUS_CHOICES = (
        (DRAFT, 'Ciorna'),
        (WAITING_APPROVAL, 'Asteapta aprobare'),
        (ACTIVE, 'Activ'),
        (DELETED, 'Sters')
    )

    user = models.ForeignKey(User, related_name='products',on_delete=models.CASCADE)
    category=models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/product_images/', blank=True, null=True)
    editie = models.IntegerField()
    editura = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    author = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

