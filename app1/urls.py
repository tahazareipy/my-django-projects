from django.urls import path
from . import views
urlpatterns = [
    path('',views.list_Product.as_view(),name="base"),
]