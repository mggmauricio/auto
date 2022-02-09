from django.contrib import admin
from .models import Category, Manufacter, Vehicle, CategoryCosts, Costs
# Register your models here.

admin.site.register(Vehicle)
admin.site.register(Category)
admin.site.register(Manufacter)
admin.site.register(CategoryCosts)
admin.site.register(Costs)