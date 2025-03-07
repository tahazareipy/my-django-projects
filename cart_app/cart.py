class Cart:
    def __init__(self, request):
        self.session = request.session
        # دریافت سبد خرید از session یا ایجاد یک سبد جدید
        cart = self.session.get('session_key', {})
        if not cart:  # اگر سبد خالی بود
            self.session['session_key'] = cart  # ایجاد کلید جدید در session
            self.session.modified = True  # علامت‌گذاری برای ذخیره session
        self.cart = cart