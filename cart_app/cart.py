from app1.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart', {})
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': str(product.price),
            }
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    def get_total_price(self):
        return sum(
            float(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
    def get_product(self):
        product_ids = self.cart.keys()
        products =Product.objects.filter(id__in=product_ids)
        return products
    def remove(self,product_id):        
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    