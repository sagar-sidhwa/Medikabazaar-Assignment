from pyexpat import model
from django.db import models

# Create your models here.
class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length =255)
    productprice = models.DecimalField(max_digits=10,decimal_places=4)
    productquantity = models.IntegerField()

    def __str__(self):
        return self.productname
