from django.urls import path
from . import views


urlpatterns = [
    path("index/", views.serve_index, name="index"),
    #path("", views.index, name="index"),
    path("list-view/", views.list_files, name="list-view"),
]












































