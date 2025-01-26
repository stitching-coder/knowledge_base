from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_entry_list, name='habit_entry_list'),
    path('entry/<int:pk>/', views.habit_entry_detail, name='habit_entry_detail'),
]
