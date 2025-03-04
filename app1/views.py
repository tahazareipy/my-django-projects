from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import Category

class list_Product(View):
    def get(self, request):
        # دریافت تمام دسته‌بندی‌ها به همراه محصولات مرتبط (بهینه‌سازی کوئری)
        categories = Category.objects.all().prefetch_related('products')
        context = {
            'categories': categories,
        }
        return render(request, 'index.html', context)
