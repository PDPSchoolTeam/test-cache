from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    post_code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.country
