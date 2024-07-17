from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=1)

    def clean(self):
        if not (1 <= self.stars <= 5):
            raise ValidationError('Stars must be between 1 and 5.')

    def __str__(self):
        return f'{self.product.title}: {self.stars} stars'
