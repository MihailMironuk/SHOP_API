from rest_framework import serializers
from product.models import Category, Product, Review
from rest_framework.exceptions import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'product', 'stars', 'id']


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['name', 'products_count', 'id']

    def get_products_count(self, obj):
        return Product.objects.filter(category=obj).count()


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price', 'reviews', 'rating']

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return sum(review.stars for review in reviews) / reviews.count()
        return 0


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255, min_length=2)
    products_count = serializers.IntegerField(required=True, min_value=0, max_value=100)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=255, min_length=2)
    description = serializers.CharField(required=True, max_length=255, min_length=2)
    category = serializers.CharField(required=True, max_length=255, min_length=2)
    price = serializers.IntegerField(required=True, min_value=4000, max_value=100000)
    reviews = serializers.CharField(required=True, max_length=255, min_length=2)
    rating = serializers.IntegerField(required=True, min_value=0, max_value=5)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=255, min_length=2)
    product = serializers.CharField(required=True, max_length=255, min_length=2)
    stars = serializers.IntegerField(required=True, min_value=0, max_value=5)


def validate(self, attrs):
    id = attrs['category_id']
    try:
        Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise ValidationError(f'Category with id ({id}) does not exist!')
    return attrs
