from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flights"),
    path("<int:flight_id>/book", views.book, name="book"),
]