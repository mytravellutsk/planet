from django.shortcuts import render
from django.urls import path, include
from . import views
from .models import Movie


urlpatterns = [
    path('avtobus', include('autotravel.urls')),
    path('', views.MoviesView.as_view(), name="index"),
    path("<slug:slug>/", views.NewsListView.as_view(), name="news_list"),
    path('proNas', views.ProNas.as_view(), name="proNas"),
    path('aviatravel', views.AviaPoshuk.as_view(), name="aviatravel"),
    path('rannebrony', views.Rannebrony.as_view(), name="rannebrony"),
]