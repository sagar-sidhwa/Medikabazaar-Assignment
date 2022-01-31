from pyrsistent import field
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        #fields = ['id','productname','productprice','productquantity']
        fields = '__all__'