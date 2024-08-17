from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name

class Purchase(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField(default=timezone.now)  # Default to current date but allows user input
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Optional
    user = models.ForeignKey(User, on_delete=models.CASCADE)