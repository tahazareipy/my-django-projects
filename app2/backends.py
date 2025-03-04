from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            validate_email(email)  # بررسی معتبر بودن ایمیل
            user = User.objects.get(email=email)  # پیدا کردن کاربر با ایمیل
            if user.check_password(password):  # بررسی رمز عبور
                return user
        except (User.DoesNotExist, ValidationError):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None