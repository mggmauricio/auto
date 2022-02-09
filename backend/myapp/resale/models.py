from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.name

class Manufacter(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name


class Vehicle(models.Model):
    category = models.ForeignKey(Category, related_name='vehicles', on_delete=models.CASCADE)
    manufacter = models.ForeignKey(Manufacter, related_name='vehicles', on_delete=models.CASCADE)
    model = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    color = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    paid_price = models.DecimalField(max_digits=15, decimal_places=2)
    costs = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    image = models.ImageField(upload_to='vehicles/%Y/%m/%d', blank=True)
    avaliable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    year = models.IntegerField(default=2021)


    def __str__(self):
        return self.model



class CategoryCosts(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Costs(models.Model):
    category = models.ForeignKey(CategoryCosts, related_name='vehicles', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.title


