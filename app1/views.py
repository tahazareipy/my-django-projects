from django.shortcuts import render
from django.views import View
from .models import Category, Product

class list_Product(View):
    def get(self, request):
        categories = Category.objects.prefetch_related('products').all()
        context = {
            'categories': categories,
        }
        return render(request, 'index.html', context)

def id_product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product_info.html', {'product': product})