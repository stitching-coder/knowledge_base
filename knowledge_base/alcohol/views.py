from django.shortcuts import render
from .models import Beverage


def beverage_list(request):
    beverages = Beverage.objects.all().order_by('-created_at')
    return render(request, 'alcohol/beverage_list.html', {'beverages': beverages})


def beverage_detail(request, pk):
    beverage = Beverage.objects.get(pk=pk)
    return render(request, 'alcohol/beverage_detail.html', {'beverage': beverage})
