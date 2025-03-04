from django.contrib import admin
from . import models

# 1. ثبت مدل‌های دیگر
admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Order)