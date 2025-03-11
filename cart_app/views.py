from django.shortcuts import render,get_object_or_404
from .cart import Cart
from app1.models import Product
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_product()
    sum_products = cart.get_total_price()
    return render(request,"cart_summary.html",{'cart_products':cart_products,'sum_products':sum_products })
@require_POST
@csrf_protect
def cart_add(request):
    cart = Cart(request)
    # دریافت و اعتبارسنجی product_id
    product_id = request.POST.get('product_id')
    if not product_id:
        return JsonResponse({'error': 'فیلد product_id ضروری است'}, status=400)
    
    try:
        product_id = int(product_id)
    except ValueError:
        return JsonResponse({'error': 'product_id نامعتبر است'}, status=400)
    
    # دریافت محصول
    product = get_object_or_404(Product, id=product_id)
    
    # افزودن به سبد خرید
    cart.add(product=product)
    # پاسخ JSON
    return JsonResponse({
        'success': True,
        'product_name': product.name,  
        'cart_items': cart.__len__()
    })

@require_POST
@csrf_protect
def cart_delete(request):
    cart = Cart(request)
    # دریافت و اعتبارسنجی product_id
    product_id = request.POST.get('product_id')
    if not product_id:
        return JsonResponse({'error': 'فیلد product_id ضروری است'}, status=400)
    
    try:
        product_id = int(product_id)
    except ValueError:
        return JsonResponse({'error': 'product_id نامعتبر است'}, status=400)
    
    # حذف از سبد خرید
    cart.remove(product_id=product_id)
    
    # محاسبه قیمت کل سبد خرید
    total_price = cart.get_total_price()
    
    
    # پاسخ JSON
    return JsonResponse({
        'success': True,
        'cart_items': cart.__len__(),
        'total_price': total_price,  # قیمت کل سبد خرید
    })

def cart_update(request):
    pass



