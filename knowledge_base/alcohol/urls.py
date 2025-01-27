from django.urls import path
from . import views

urlpatterns = [
    path('', views.beverage_list, name='beverage_list'),
    path('beverage/<int:pk>/', views.beverage_detail, name='beverage_detail'),
]
