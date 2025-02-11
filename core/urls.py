from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('auth/', include('accounts.path')),
    path('inventory/', include('inventory.path')),
    path("accounts/", include("django.contrib.auth.urls")),
]
