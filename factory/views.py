from django.shortcuts import render
from rest_framework import generics

from factory.models import Supplier
from factory.serializers import SupplierSerializer


class SupplierCreateAPIView(generics.CreateAPIView):
    """ Create """
    serializer_class = SupplierSerializer


class SupplierListAPIView(generics.ListAPIView):
    """ List View """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """ Show One """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """ Update """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierDestroyAPIView(generics.DestroyAPIView):
    """ Delete """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
