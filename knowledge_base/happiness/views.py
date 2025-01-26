from django.shortcuts import render
from .models import Entry


def entry_list(request):
    entries = Entry.objects.all().order_by('-created_at')
    return render(request, 'happiness/entry_list.html', {'entries': entries})


def entry_detail(request, pk):
    entry = Entry.objects.get(pk=pk)
    return render(request, 'happiness/entry_detail.html', {'entry': entry})
