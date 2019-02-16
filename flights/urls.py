from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="flight_index"),
    path("<int:flight_id>",views.flight,name="flight"),
    path("<int:flight_id>/book",views.book,name="book"),
    path("<int:flight_id>/<int:passenger_id>/cancel",views.cancel,name="cancel")
]
