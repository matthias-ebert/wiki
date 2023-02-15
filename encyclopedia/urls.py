from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry_name>", views.entry, name="index"),
    path("results", views.search, name="search")
]
