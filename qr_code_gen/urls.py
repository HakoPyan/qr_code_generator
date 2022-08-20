from django.urls import path
from . import views

urlpatterns = [
    path("qr_form/", views.qr_form, name="qr_form"),
    path("qr/", views.show_qr, name="show_qr"),
    path("add/", views.add_qr, name="add_qr"),
]