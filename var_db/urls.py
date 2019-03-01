from django.conf.urls import url, include
from django.urls import path
from var_db import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_variant, name='search_variant'),
    path('edit/<int:pk>/', views.edit_variant, name='edit_variant'),
    path('add/', views.add_variant, name='add_variant'),
    path('upload/', views.upload_file, name='upload_file')

]