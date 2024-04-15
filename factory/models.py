from django.db import models


class Supplier(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.name


class NetworkNode(models.Model):

    FACTORY = 0
    RETAILER = 1
    INDIVIDUAL = 2

    NODE_CHOICES = [
        (FACTORY, 'Factory'),
        (RETAILER, 'Retailer'),
        (INDIVIDUAL, 'Individual')
    ]

    node_type = models.IntegerField(choices=NODE_CHOICES)
    name = models.CharField(max_length=100)

    contacts_email = models.EmailField()
    contacts_country = models.CharField(max_length=100)
    contacts_city = models.CharField(max_length=100)
    contacts_street = models.CharField(max_length=100)
    contacts_house_number = models.CharField(max_length=10)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)

    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
