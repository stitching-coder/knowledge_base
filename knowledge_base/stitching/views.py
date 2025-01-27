from django.shortcuts import render
from .models import StitchingProjectEntry


def stitching_entry_list(request):
    entries = StitchingProjectEntry.objects.all().order_by('-created_at')
    return render(request, 'stitching/stitching_entry_list.html', {'entries': entries})


def stitching_entry_detail(request, pk):
    entry = StitchingProjectEntry.objects.get(pk=pk)
    return render(request, 'stitching/stitching_entry_detail.html', {'entry': entry})
