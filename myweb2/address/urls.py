from address import views
from django.urls import path
urlpatterns = [
    path('', views.home),         # http://localhost/address
    path('write', views.write),   # http://localhost/write
    path('insert', views.insert), # http://localhost/insert
    path('update', views.update), # http://localhost/update
    path('delete', views.delete), # http://localhost/delete
    path('detail', views.detail), # http://localhost/detail
]