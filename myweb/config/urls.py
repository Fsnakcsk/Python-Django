
from django.contrib import admin
from django.urls import path, include
from config import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home),
    path('address/', include('address.urls')),
    path('memo/', include('memo.urls')),
]
