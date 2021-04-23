from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    # path('create/', views.TodoCreate.as_view(), name="create"),  
    # path('delete/<int:todo_id>/', views.delete, name="delete"),  
]