from django.urls import path
from . import views

urlpatterns = [
    path('<slug:group_name>/', views.index),
]