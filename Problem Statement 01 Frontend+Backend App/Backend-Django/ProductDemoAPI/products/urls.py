from django.urls import path
from .views import product_list,ProductAPIView,ProductDetailsAPIView

urlpatterns = [
    #path('product/', product_list),
    path('product/', ProductAPIView.as_view()),
    path('productdetails/<int:id>/', ProductDetailsAPIView.as_view()),
]