from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cart/',include('cart_app.urls')),
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include('app2.urls')),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
