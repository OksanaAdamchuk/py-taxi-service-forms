from django.urls import path

from .views import (
    CarCreateView,
    CarDeleteView,
    CarUpdateView,
    ManufacturerCreateView,
    ManufacturerDeleteView,
    ManufacturerUpdateView,
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path(
        "manufacturers/create/", ManufacturerCreateView.as_view(),
        name="manufacturer-create"
    ),
    path(
        "manufacturers/<int:pk>/update/", ManufacturerUpdateView.as_view(),
        name="manufacturer-update"
    ),
    path(
        "manufacturers/<int:pk>/delete/", ManufacturerDeleteView.as_view(),
        name="manufacturer-delete"
    ),
]

app_name = "taxi"
