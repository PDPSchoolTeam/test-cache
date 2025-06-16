from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
] + debug_toolbar_urls()


