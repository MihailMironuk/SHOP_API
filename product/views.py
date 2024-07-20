from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from product.models import Category, Product, Review


@api_view(['GET', 'POST'])
def categories_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(name=name)
        category.save()
        return Response(status=status.HTTP_201_CREATED, data={'category_id': category.id})


@api_view(['GET', 'POST', ])
def products_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductSerializer(products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category')

        product = Product.objects.create(
            title=title,
            description=description,
            category_id=category_id,
            price=price,
        )

        product.save()
        return Response(status=status.HTTP_201_CREATED, data={'product_id': product.id})


@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={'review_id': review.id})
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'Error message': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = ReviewSerializer(review, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'review_id': review.id})


@api_view(['GET', 'PUT', 'DELETE'])
def categories_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'Error message': 'Category not found'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = CategorySerializer(category, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'category_id': category.id})


@api_view(['GET', 'PUT', 'DELETE'])
def products_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'Error message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = ProductSerializer(product, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data={'product_id': product.id})
