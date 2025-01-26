from django.shortcuts import render
from .models import AlcoholEntry


def alcohol_entry_list(request):
    entries = AlcoholEntry.objects.all().order_by('-created_at')
    return render(request, 'alcohol/alcohol_entry_list.html', {'entries': entries})


def alcohol_entry_detail(request, pk):
    entry = AlcoholEntry.objects.get(pk=pk)
    return render(request, 'alcohol/alcohol_entry_detail.html', {'entry': entry})
