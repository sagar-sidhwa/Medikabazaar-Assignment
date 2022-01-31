from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from numpy import product
from rest_framework.parsers import JSONParser
from .models import Product
from .serializers import ProductSerializer
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
#@csrf_exempt
class ProductAPIView(APIView):

    def get(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#@csrf_exempt
class ProductDetailsAPIView(APIView):

    def get_object(self,id):
        try:
            return Product.objects.get(pid=id)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        product = self.get_object(id)
        seralizer = ProductSerializer(product)
        return Response(seralizer.data)
    
    def put(self,request,id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        product = self.get_object(id)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


def product_list(request):
    return "Ok"