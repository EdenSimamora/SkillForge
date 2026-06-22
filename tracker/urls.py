from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_skill, name='add'),
    path('delete/<int:pk>/', views.delete_skill, name='delete'),
]