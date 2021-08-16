from django.shortcuts import render
from django.views import View
from .models import Travels


class TravelList(View):
    def get(self, request):
        avtobus = Travels.objects.order_by('id')
        return render(request, 'autotravel/avtobus.html', {'avtobus': avtobus})


class TravelListView(View):
    def get(self, request, slug):
        avtobus = Travels.objects.get(url=slug)
        return render(request, 'autotravel/avtobustravel.html', {'avtobus': avtobus})