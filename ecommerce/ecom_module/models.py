from django.db import models


class Category(models.Model):
    """
    Model for category.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey('self', null=True, default=None)

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    Model for items.
    """
    subcategory = models.ForeignKey('Category')
    category = models.ForeignKey('Category', related_name='category_name')
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    specification = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    """
    Model for cart.
    """
    owner = models.ForeignKey('auth.User')
    item = models.ManyToManyField(Item)
    quantity = models.IntegerField()
    total_price = models.IntegerField()






