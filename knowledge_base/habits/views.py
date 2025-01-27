from django.shortcuts import render
from .models import Habit


def habit_list(request):
    habits = Habit.objects.all().order_by('-created_at')
    return render(request, 'habits/habit_list.html', {'habits': habits})


def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'habits/habit_detail.html', {'habit': habit})
