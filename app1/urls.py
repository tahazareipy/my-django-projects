from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_Product.as_view(), name="base"),
    path('product/<int:pk>', views.id_product, name="id-product"),
]

#اضافه کردن فیلتر