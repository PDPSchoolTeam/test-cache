from django.shortcuts import render
from api.models import Address
from django.views.decorators.cache import cache_page


@cache_page(60 * 1)
def address_list(requests):
    addresses = Address.objects.all()
    return render(requests, 'home.html', {'addresses': addresses})
