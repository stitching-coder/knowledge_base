from django.urls import path
from . import views

urlpatterns = [
    path('', views.stitching_entry_list, name='entry_list'),
    path('entry/<int:pk>/', views.stitching_entry_detail, name='entry_detail'),
]
