from django.urls import path
from api.views import address_list

urlpatterns = [
    path("", address_list)
]
