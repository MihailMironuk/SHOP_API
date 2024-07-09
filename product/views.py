from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from product.models import Category, Product, Review


# Для вывода всех категорий
@api_view(http_method_names=['GET'])
def categories_list_api_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


# Для вывода одной категории
@api_view(['GET'])
def categories_detail_api_view(request, id):
    categories = Category.objects.get(id=id)
    data = CategorySerializer(categories, many=False).data
    return Response(data=data)


# Для вывода всех товаров
@api_view(http_method_names=['GET'])
def products_list_api_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


# Для вывода одного товара
@api_view(['GET'])
def products_detail_api_view(request, id):
    products = Product.objects.get(id=id)
    data = ProductSerializer(products, many=False).data
    return Response(data=data)


# Для вывода всех отзывов
@api_view(http_method_names=['GET'])
def reviews_list_api_view(request):
    views = Review.objects.all()
    data = ReviewSerializer(views, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


# Для вывода одного отзыва
@api_view(['GET'])
def reviews_detail_api_view(request, id):
    views = Review.objects.get(id=id)
    data = ReviewSerializer(views, many=False).data
    return Response(data=data)
