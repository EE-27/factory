from django.urls import path

from factory.apps import FactoryConfig
from factory.views import SupplierListAPIView, SupplierCreateAPIView, SupplierRetrieveAPIView, SupplierUpdateAPIView, \
    SupplierDestroyAPIView

app_name = FactoryConfig.name

urlpatterns = [
    path("suppliers/", SupplierListAPIView.as_view(), name="suppliers-list"),
    path("suppliers/create/", SupplierCreateAPIView.as_view(), name="suppliers-create"),
    path("suppliers/<int:pk>/", SupplierRetrieveAPIView.as_view(), name="suppliers-retrieve"),
    path("suppliers/update/<int:pk>/", SupplierUpdateAPIView.as_view(), name="suppliers-update"),
    path("suppliers/delete/<int:pk>/", SupplierDestroyAPIView.as_view(), name="suppliers-delete")
]