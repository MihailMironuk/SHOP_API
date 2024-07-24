from django.urls import path
from product import views

urlpatterns = [
    path('', views.categories_list_api_view),
    path('<int:id>/', views.categories_detail_api_view)
]