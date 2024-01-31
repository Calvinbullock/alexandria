from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.serve_index),
    path("", views.index, name="index"),
]












































