from django.urls import path, include
from member import views

urlpatterns = [
    path('', views.home),
    path('add_vip', views.add_vip),
    path('insert', views.insert),
    path('login', views.login),
    path('logout', views.logout),
]