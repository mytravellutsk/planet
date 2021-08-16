from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import NewsList


class MoviesView(View):
    def get(self, request):
        news = NewsList.objects.all()
        return render(request, 'main/index.html', {'news': news})


class NewsListView(View):
    def get(self, request, slug):
        news = NewsList.objects.get(url=slug)
        return render(request, 'main/news_list.html', {'news': news})


class ProNas(View):
    def get(self, request):
        return render(request, 'main/proNas.html')


class AviaPoshuk(View):
    def get(self, request):
        return render(request, 'main/aviatravel.html')


class Rannebrony(View):
    def get(self, request):
        return render(request, 'main/rannebrony.html')