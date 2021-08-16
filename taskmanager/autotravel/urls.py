from django.shortcuts import render
from django.urls import path
from . import views
from .models import Movie


urlpatterns = [
    path('avtobus', views.TravelList.as_view(), name="avtobus"),
    path("<slug:slug>/", views.TravelListView.as_view(), name="avtobus_list"),
]