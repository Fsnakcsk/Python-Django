from django.urls import path
from address import views


urlpatterns = [
    path('', views.home),
    path('write', views.write),
    path('insert', views.insert),
    path('update', views.update),
    path('delete', views.delete),
    path('detail', views.detail),
]
