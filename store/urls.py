from django.urls import path

from . import views 

urlpatterns = [
    # path('category_detail/<slug:slug>/', views.category_detail, name='category_detail'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
]