from django.urls import path
from . import views

urlpatterns = [
    path('', views.alcohol_entry_list, name='alcohol_entry_list'),
    path('entry/<int:pk>/', views.alcohol_entry_detail, name='alcohol_entry_detail'),
]
