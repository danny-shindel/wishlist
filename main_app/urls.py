from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('add/', views.Add.as_view(), name="add"),  
    path('delete/<int:wish_id>/', views.delete, name="delete"),  
]