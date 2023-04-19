from django.urls import path

from . import views

urlpatterns = [
    path("offers/", views.ListOffersView.as_view()),
]
