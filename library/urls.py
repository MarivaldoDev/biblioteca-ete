from django.urls import path
from library import views

urlpatterns = [
    path('', views.first, name='first'),
    path('criar/', views.criar, name='criar')
]