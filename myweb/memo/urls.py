
from django.contrib import admin
from django.urls import path, include
from memo import views

urlpatterns = [
    path('', views.home),
    path('insert_memo', views.insert_memo),
    path('detail', views.detail),
    path('update_memo', views.update_memo),
    path('delete_memo', views.delete_memo),


]
