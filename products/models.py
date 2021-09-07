from django.db import models
from django.contrib.auth import get_user_model

class Product(models.Model):
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.name
