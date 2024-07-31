from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories_list_api_view),
    path('<int:id>/', views.categories_detail_api_view),
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:id>/', views.CategoryDetailAPIView.as_view()),
    path('products/', views.ProductListCreateAPIView.as_view()),
    path('products/<int:id>/', views.ProductDetailAPIView.as_view()),
    path('reviews/', views.ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
]
