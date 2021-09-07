from django.db import models
from django.contrib.auth import get_user_model

class Product(models.Model):
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name
