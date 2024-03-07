from django.db import models


# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(null=False, default=1)

    def __str__(self):
        return f'{self.name} {self.id}'
