from django.shortcuts import render
from .models import HabitEntry


def habit_entry_list(request):
    entries = HabitEntry.objects.all().order_by('-created_at')
    return render(request, 'habits/habit_entry_list.html', {'entries': entries})


def habit_entry_detail(request, pk):
    entry = HabitEntry.objects.get(pk=pk)
    return render(request, 'habits/habit_entry_detail.html', {'entry': entry})

# Create your views here.
